import numpy as np
import pandas as pd

def genre_avg_duration(movies_df,genre):
    # Select subset of records with the specified genre
    genre_subset = movies_df[movies_df['first_genre'] == genre]
    
    # Calculate the average duration of movies in the genre
    avg_duration = genre_subset['duration'].mean()
    
    return avg_duration


if __name__ == "__main__":
    # Read in the movies data
    movies_df = pd.read_csv("IMDb movies.csv")
    movies_df.info()

    # Split the 'genre' column by commas and select the first part (the first genre)
    movies_df['first_genre'] = movies_df['genre'].str.split(',').str[0]

    avg_duration = genre_avg_duration('Comedy')
    print("Average duration is: {}".format(movies_df,avg_duration))
