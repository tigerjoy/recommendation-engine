from dao.averageRatingDAO import AverageRatingDAO
from update_data import update_average_ratings_data as uard
from get_data import get_average_rating_data as gard
import constant_paths


def add_average_rating_data(movieId: int, avgRating: float) -> bool:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    # If average rating data already exists, update the entry in table
    if gard.get_average_rating_by_movie(movieId) is not None:
        return uard.update_average_rating_data(movieId, avgRating)
    # If average rating does not exist, add it to the table
    else:
        the_avg_rating = AverageRatingDAO(movieId, avgRating)
        return dao.addAverageRatingByMovie(the_avg_rating)
