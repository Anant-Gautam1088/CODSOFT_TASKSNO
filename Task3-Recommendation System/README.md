# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Flask, Pandas, and Scikit-learn. The application recommends the top 5 similar movies based on the user's selected movie using cosine similarity.

## Features

- 🎥 Recommend Top 5 similar movies
- 🎯 Content-Based Recommendation System
- 📚 TMDB 5000 Movies Dataset
- 🖥️ Interactive Flask Web Application
- 🎨 Modern Responsive UI
- ⚡ Fast recommendations using Cosine Similarity

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS

## Machine Learning Concepts

- Content-Based Filtering
- Count Vectorization
- Cosine Similarity
- Text Preprocessing

## Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── model.py
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```
## Dataset

This project uses the TMDB 5000 Movies Dataset.

Download the following files and place them in the project root directory before running the project:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv
  
## Installation

```bash
pip install -r requirements.txt
```

Run the model:

```bash
python model.py
```

Start the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Future Improvements

- Movie Posters
- Movie Ratings
- Genre Information
- Release Year
- TMDB API Integration
- Search Autocomplete

## Author

ANANT GAUTAM
