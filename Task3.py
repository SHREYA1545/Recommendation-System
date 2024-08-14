import pandas as pd

# Sample data: Movies and their genres
data = {
   'movie': ['Aranmanai 4','Maya', 'English Vinglish','Gol Maal','Singham','Action',' Lapata Ladies','Bad News','Stree 2','3 idiots'
              ,'Jab we met','Love Aaj Kal','Pink','Panga','Dangal'],
    'genres': ['Horror','Horror','Family','comedy','action','action','family','comedy','Horror','Family','Family','Romantic','Girl','Girl','Girl']
}

# Create DataFrame
df = pd.DataFrame(data)

def recommend_similar_movies(movie_title, num_recommendations=3):
    # Ensure the movie title exists in the dataset
    if movie_title not in df['movie'].values:
        return f"Movie '{movie_title}' not found in the database."
    
    # Get the genres of the given movie
    movie_genres = df[df['movie'] == movie_title]['genres'].values[0]
    
    # Find movies with at least one matching genre
    recommendations = df[df['genres'].str.contains('|'.join(movie_genres.split(', ')), case=False)]
    
    # Exclude the given movie from the recommendations
    recommendations = recommendations[recommendations['movie'] != movie_title]
    
    # Return top N recommendations
    return recommendations['movie'].head(num_recommendations).tolist()

# User input
movie_title = input("Enter a movie title: ")
recommendations = recommend_similar_movies(movie_title)

if isinstance(recommendations, list):
    print(f"Recommendations similar to '{movie_title}':")
    print(recommendations)
else:
    print(recommendations)