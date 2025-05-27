# 🎬 Movie Recommendation System using Neo4j and Flask

## 📖 Overview
This project is a simple movie recommendation system built using the Neo4j graph database and a Flask web application.  
It leverages the [MovieLens dataset](https://grouplens.org/datasets/movielens/latest/) to load movies, genres, and user ratings into Neo4j, and provides two types of recommendations for users:

- **Genre-based recommendations**: Movies from genres a user likes but hasn’t rated yet.
- **Collaborative filtering recommendations**: Movies liked by users with similar tastes.

---

## 🚀 Features
- Load movies and user ratings into Neo4j using Python scripts.
- Use Cypher queries to generate smart recommendations.
- Web interface built with Flask, HTML, and CSS.
- Responsive and minimal UI.
- Two recommendation algorithms:
  - Genre-based
  - Collaborative filtering

---

## 🧰 Prerequisites
- Python 3.7 or higher
- Neo4j (Community or Enterprise Edition) installed and running
- `pip` for installing Python dependencies
- MovieLens dataset (movies and ratings)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/VnMxMadMax/demo-projects/tree/main/neo4j
cd neo4j
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:
```
flask
neo4j
pandas
python-dotenv
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory with your Neo4j credentials:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

Replace with your actual Neo4j instance details.

### 4. Download MovieLens Dataset
Download and place the following files into a `data/` folder:

- `movies.csv`
- `ratings.csv`

You can get them from the [MovieLens official site](https://grouplens.org/datasets/movielens/latest/).

### 5. Load Data into Neo4j
Run the loader script to import data into Neo4j:

```bash
python load_movielens.py
```

### 6. Run the Flask Application
Start the Flask server:

```bash
python app.py
```

Then open your browser and go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Usage

- Enter a valid **user ID** (integer) from the MovieLens dataset (e.g., `1`, `10`, `100`).
- Submit the form.
- You'll receive:
  - 🎭 **Genre-Based Recommendations** – based on genres the user likes but hasn't rated movies from yet.
  - 🤝 **Collaborative Filtering Recommendations** – based on movies liked by users with similar preferences.

---

## 📁 Project Structure
```bash
├── app.py                 # Flask app main script
├── query_engine.py        # Neo4j queries for recommendations
├── load_movielens.py      # Script to load MovieLens data into Neo4j
├── templates/
│   └── index.html         # Frontend HTML template
├── data/
│   ├── movies.csv         # MovieLens movies data
│   └── ratings.csv        # MovieLens ratings data
├── .env                   # Environment variables (not committed)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🔧 Possible Improvements
- Add user authentication for personalized sessions
- Cache recommendations to improve performance
- Include more detailed movie info (e.g., posters, descriptions via external APIs)
- Support additional recommendation strategies (e.g., content-based, matrix factorization)
- Containerize the app with Docker for easy deployment

---

## 🐳 (Optional) Docker Support
You can containerize the application for easier setup:

**Dockerfile**
```Dockerfile
# Example Dockerfile (not included in repo)
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t movie-recommender .
docker run -p 5000:5000 --env-file .env movie-recommender
```

---

## 📄 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Author
Created by **[Hammadur Rahman]**  
Feel free to contribute, report issues, or suggest improvements!
