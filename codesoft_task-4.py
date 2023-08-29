
import pandas as pd

# Load the MovieLens dataset
data = pd.read_csv('ratings.csv') 

# Explore the dataset
print(data.head())

# Create a user-item matrix
user_item_matrix = data.pivot_table(index='userId', columns='movieId', values='rating')

# Fill missing values with 0 (meaning no rating)
user_item_matrix = user_item_matrix.fillna(0)

# Calculate user similarity using Pearson correlation
user_similarity = user_item_matrix.corr()

# Function to get movie recommendations for a user
def get_movie_recommendations(user_id, top_n=5):
    user_ratings = user_item_matrix.loc[user_id]
    similar_users = user_similarity[user_id]
    
    # Filter out movies the user has already rated
    movies_already_rated = user_ratings[user_ratings > 0].index
    
    # Calculate the weighted sum of ratings from similar users
    recommendations = user_similarity[user_id] * user_item_matrix[movies_already_rated]
    
    # Sum the weighted ratings and sort by highest to lowest
    recommendations = recommendations.sum(axis=1).sort_values(ascending=False)
    
    # Filter out movies the user has already rated
    recommendations = recommendations[~recommendations.index.isin(movies_already_rated)]
    
    return recommendations.head(top_n)

# Get recommendations for a user (change the user_id as needed)
user_id = 1
recommendations = get_movie_recommendations(user_id)
print(f"Top 5 movie recommendations for User {user_id}:\n{recommendations}")



