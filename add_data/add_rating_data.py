from dao.ratingDAO import RatingDAO
from core.rating import Rating
from update_data import update_ratings_data as urd
import constant_paths


def add_rating_data(userId: int, movieId: int, rating: float) -> bool:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    # If rating data already exists, update the entry in table
    if len(dao.searchByUserIDMovieID(userId, movieId)) != 0:
        return urd.update_rating_data(userId, movieId, rating)
    # If rating does not exist, add it to the table
    else:
        the_rating = Rating(userId, movieId, rating)
        return dao.addRatingByUser(the_rating)
