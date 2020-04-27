from core.rating import Rating
from dao.ratingDAO import RatingDAO
from typing import List
import constant_paths


# Added get_rating_by_user_movie() to retrieve the rating against a user_id and movie_id
def get_rating_by_user_movie(user_id: int, movie_id: int) -> Rating:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    output = dao.searchByUserIDMovieID(user_id, movie_id)
    if len(output) > 0:
        return output[0]
    else:
        return None


# To get_average_rating_by_id() to calculate the current average rating of a movie
def get_average_rating_by_movie(movie_id: int) -> float:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.calculateAverageRatingByMovie(movie_id)


# To get movie_id and rating information of movies seen by user
def get_movies_seen_by_user(user_id: int) -> List[Rating]:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.searchByUserID(user_id)
