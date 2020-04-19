from core.genre import Genre
from core.averageRating import AverageRating
from dao.averageRatingDAO import AverageRatingDAO
from typing import List
import constant_paths


def get_movies_of_genres_seen_by_user(genre_list: List[Genre], user_id: int) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesSeenByUser(genre_list, user_id)


def get_movies_by_genres(genre_list: List[Genre], ascending: bool = False) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesFromGenres(genre_list, ascending)
