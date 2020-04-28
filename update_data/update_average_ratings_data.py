from dao.averageRatingDAO import AverageRatingDAO
from core.averageRating import AverageRating
import constant_paths


def update_average_rating_data(movieId: int, avgRating: float) -> bool:
    the_avg_rating = AverageRating(movieId, avgRating)
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)

    return dao.updateAverageRatingByMovie(the_avg_rating)
