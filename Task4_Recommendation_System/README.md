# Task 4 — Recommendation System

## Objective
Create a simple recommendation system that suggests items to users based on
their preferences, using collaborative or content-based filtering.

## Approach (Content-Based Filtering)
- Each movie is represented by a "tags" string combining its genres and
  keywords.
- `TfidfVectorizer` converts these tag strings into TF-IDF feature vectors.
- `cosine_similarity` computes pairwise similarity between all movies.
- Given a movie title, the system returns the `N` most similar movies
  (excluding the movie itself).

## How to run
```bash
pip install -r requirements.txt
python recommender.py
```
Enter one of the listed movie titles when prompted to get recommendations.

## Example
```
Enter a movie title to get recommendations: The Dark Knight

Because you liked 'The Dark Knight', you might also enjoy:
  1. Batman Begins
  2. John Wick
  3. Inception
```

## Concepts demonstrated
- Content-based filtering
- TF-IDF vectorization
- Cosine similarity for measuring item similarity

## Possible extensions
- Swap in a real dataset (e.g., MovieLens 100k/1M)
- Add collaborative filtering (user-item rating matrix + matrix factorization)
- Build a hybrid recommender combining both approaches
- Wrap in a small Streamlit app for an interactive UI
