import pandas as pd
from function_genre_avg_duration import genre_avg_duration

def test_genre_avg_duration():
    # Sample data for testing
    data = {'first_genre': ['Comedy', 'Comedy', 'Drama', 'Action'],
            'duration': [90, 95, 120, 110]}
    movies_df = pd.DataFrame(data)

    # Test case 1: Calculate the average duration for 'Comedy' genre
    avg_duration = genre_avg_duration(movies_df,'Comedy')
    assert avg_duration == 92.5  # Expected average duration for 'Comedy' genre

    # Test case 2: Calculate the average duration for 'Drama' genre
    avg_duration = genre_avg_duration(movies_df,'Drama')
    assert avg_duration == 120.0  # Expected average duration for 'Drama' genre

    # Test case 3: Calculate the average duration for a genre not in the dataset
    avg_duration = genre_avg_duration(movies_df,'Science Fiction')
    assert pd.isna(avg_duration)  # Expected result is NaN since the genre is not in the dataset