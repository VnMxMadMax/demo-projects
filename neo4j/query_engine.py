from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class MovieRecommender:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
        )

    def close(self):
        self.driver.close()

    def recommend_by_genre(self, user_id, limit=5):
        with self.driver.session() as session:
            result = session.execute_read(self._recommend_by_genre, user_id, limit)
            return result

    def recommend_by_user_similarity(self, user_id, limit=5):
        with self.driver.session() as session:
            result = session.execute_read(self._recommend_by_similar_users, user_id, limit)
            return result

    @staticmethod
    def _recommend_by_genre(tx, user_id, limit):
        query = """
        MATCH (u:User {id: $user_id})-[:RATED]->(:Movie)-[:IN_GENRE]->(g:Genre)<-[:IN_GENRE]-(rec:Movie)
        WHERE NOT EXISTS {
            MATCH (u)-[:RATED]->(rec)
        }
        RETURN rec.title AS title, COUNT(*) AS score
        ORDER BY score DESC
        LIMIT $limit
        """
        result = tx.run(query, user_id=user_id, limit=limit)
        return [(record["title"], record["score"]) for record in result]

    @staticmethod
    def _recommend_by_similar_users(tx, user_id, limit):
        query = """
        MATCH (u1:User {id: $user_id})-[:RATED]->(m:Movie)<-[:RATED]-(u2:User)
        WHERE u1 <> u2
        WITH u1, u2, COUNT(m) AS common_movies
        ORDER BY common_movies DESC
        LIMIT 10

        MATCH (u2)-[r:RATED]->(rec:Movie)
        WHERE NOT EXISTS {
            MATCH (u1)-[:RATED]->(rec)
        } AND r.rating >= 4.0

        RETURN DISTINCT rec.title AS title, AVG(r.rating) AS avg_rating
        ORDER BY avg_rating DESC
        LIMIT $limit
        """
        result = tx.run(query, user_id=user_id, limit=limit)
        return [(record["title"], round(record["avg_rating"], 2)) for record in result]

# ------------------------------------------
# CLI Usage Starts Here
# ------------------------------------------

if __name__ == "__main__":
    try:
        user_input = input("🔢 Enter a user ID to get recommendations: ")
        user_id = int(user_input)

        recommender = MovieRecommender()

        print(f"\n🎬 Genre-based recommendations for User {user_id}:")
        genre_recs = recommender.recommend_by_genre(user_id)
        for title, score in genre_recs:
            print(f"⭐ {title} (genre match score: {score})")

        print(f"\n👥 Collaborative filtering for User {user_id}:")
        collab_recs = recommender.recommend_by_user_similarity(user_id)
        for title, avg_rating in collab_recs:
            print(f" {title} (avg rating: {avg_rating})")

    except ValueError:
        print("❌ Invalid user ID. Please enter a valid number.")
    finally:
        if 'recommender' in locals():
            recommender.close()
