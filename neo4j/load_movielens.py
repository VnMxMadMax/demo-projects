import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class MovieLensLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_movies(self, movies_df):
        with self.driver.session() as session:
            for _, row in movies_df.iterrows():
                title = row['title']
                movie_id = int(row['movieId'])
                genres = row['genres'].split('|') if row['genres'] else []
                session.write_transaction(self._create_movie_node, movie_id, title, genres)

    def load_ratings(self, ratings_df):
        with self.driver.session() as session:
            for _, row in ratings_df.iterrows():
                user_id = int(row['userId'])
                movie_id = int(row['movieId'])
                rating = float(row['rating'])
                session.write_transaction(self._create_rating_relationship, user_id, movie_id, rating)

    @staticmethod
    def _create_movie_node(tx, movie_id, title, genres):
        tx.run("""
        MERGE (m:Movie {id: $movie_id})
        SET m.title = $title
        WITH m
        UNWIND $genres AS genre
        MERGE (g:Genre {name: genre})
        MERGE (m)-[:IN_GENRE]->(g)
        """, movie_id=movie_id, title=title, genres=genres)

    @staticmethod
    def _create_rating_relationship(tx, user_id, movie_id, rating):
        tx.run("""
        MERGE (u:User {id: $user_id})
        MERGE (m:Movie {id: $movie_id})
        MERGE (u)-[r:RATED]->(m)
        SET r.rating = $rating
        """, user_id=user_id, movie_id=movie_id, rating=rating)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    URI = os.getenv("NEO4J_URI")
    USERNAME = os.getenv("NEO4J_USERNAME")
    PASSWORD = os.getenv("NEO4J_PASSWORD")

    loader = MovieLensLoader(URI, USERNAME, PASSWORD)

    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")

    print("📥 Inserting movies...")
    loader.load_movies(movies)

    print("📥 Inserting ratings...")
    loader.load_ratings(ratings)

    print("✅ MovieLens data loaded successfully!")
    loader.close()

