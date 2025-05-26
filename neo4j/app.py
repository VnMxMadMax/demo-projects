from flask import Flask, render_template, request
from query_engine import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender()

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = {
        "genre": [],
        "collab": [],
    }
    user_id = None

    if request.method == 'POST':
        user_id = request.form['user_id']
        try:
            user_id = int(user_id)
            recommendations["genre"] = recommender.recommend_by_genre(user_id)
            recommendations["collab"] = recommender.recommend_by_user_similarity(user_id)
        except ValueError:
            user_id = None

    return render_template("index.html", recommendations=recommendations, user_id=user_id)

@app.teardown_appcontext
def close_db(error):
    recommender.close()

if __name__ == '__main__':
    app.run(debug=True)
