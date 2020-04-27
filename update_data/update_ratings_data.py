from dao.ratingDAO import RatingDAO
from core.rating import Rating
import constant_paths


def update_rating_data(userId: int, movieId: int, rating: float) -> bool:
    the_rating = Rating(userId, movieId, rating)
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)

    return dao.updateRatingByUser(the_rating)
