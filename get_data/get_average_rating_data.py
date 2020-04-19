from core.genre import Genre
from core.averageRating import AverageRating
from dao.averageRatingDAO import AverageRatingDAO
from typing import List
import constant_paths


def get_movies_of_genres_seen_by_user(genre_list: List[Genre], user_id: int, ascending: bool = False) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesSeenByUser(genre_list, user_id, ascending)


def get_movies_of_genres_not_seen_user(genre_list: List[Genre], user_id: int, ascending: bool = False) -> List[AverageRating]:
    movies_from_users_favourite_genre = get_movies_by_genres(genre_list, ascending)
    users_seen_movies = get_movies_of_genres_seen_by_user(genre_list, user_id, ascending)
    return set(movies_from_users_favourite_genre).difference(users_seen_movies)


def get_movies_by_genres(genre_list: List[Genre], ascending: bool = False) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesFromGenres(genre_list, ascending)
