"""
CODSOFT - Task 4: Recommendation System
-------------------------------------------
A simple content-based movie recommendation system. It recommends movies
similar to a given movie using cosine similarity over genre/keyword
features (TF-IDF vectors).

Run:
    python recommender.py
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# ---------------------------------------------------------------------
# Small sample dataset (title + combined "tags": genres & keywords).
# In a real project you'd load this from a CSV (e.g. MovieLens dataset).
# ---------------------------------------------------------------------
DATA = [
    {"title": "The Matrix", "tags": "action sci-fi hacker dystopia virtual reality"},
    {"title": "Inception", "tags": "action sci-fi dream heist thriller mind-bending"},
    {"title": "Interstellar", "tags": "sci-fi space time travel drama exploration"},
    {"title": "The Dark Knight", "tags": "action crime superhero thriller batman"},
    {"title": "Batman Begins", "tags": "action superhero origin batman thriller"},
    {"title": "The Notebook", "tags": "romance drama love story emotional"},
    {"title": "Titanic", "tags": "romance drama tragedy love story ship"},
    {"title": "Toy Story", "tags": "animation family comedy adventure friendship"},
    {"title": "Finding Nemo", "tags": "animation family adventure ocean friendship"},
    {"title": "John Wick", "tags": "action revenge assassin thriller gun-fu"},
]


class ContentRecommender:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["tags"])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def recommend(self, title, top_n=3):
        if title not in self.df["title"].values:
            return []

        idx = self.df.index[self.df["title"] == title][0]
        scores = list(enumerate(self.similarity_matrix[idx]))
        # exclude the movie itself, sort by similarity descending
        scores = sorted(
            [s for s in scores if s[0] != idx],
            key=lambda x: x[1],
            reverse=True,
        )
        top_indices = [i for i, _ in scores[:top_n]]
        return self.df.iloc[top_indices]["title"].tolist()


def main():
    recommender = ContentRecommender(DATA)

    print("Available movies:")
    for title in recommender.df["title"]:
        print(f"  - {title}")

    print()
    movie = input("Enter a movie title to get recommendations: ").strip()
    recommendations = recommender.recommend(movie, top_n=3)

    if not recommendations:
        print("Movie not found in the dataset. Try one from the list above.")
        return

    print(f"\nBecause you liked '{movie}', you might also enjoy:")
    for i, rec in enumerate(recommendations, start=1):
        print(f"  {i}. {rec}")


if __name__ == "__main__":
    main()
