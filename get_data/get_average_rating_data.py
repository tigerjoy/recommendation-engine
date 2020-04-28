from core.genre import Genre
from core.averageRating import AverageRating
from dao.averageRatingDAO import AverageRatingDAO
from typing import List
import constant_paths
import collections
import json


class OrderedSet(collections.abc.Set):
    def __init__(self, iterable=()):
        self.d = collections.OrderedDict.fromkeys(iterable)

    def __len__(self):
        return len(self.d)

    def __contains__(self, element):
        return element in self.d

    def __iter__(self):
        return iter(self.d)


def get_all_movies_by_average_rating(ascending: bool = False) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.getAllAverageRatings(ascending)


def get_movies_of_genres_seen_by_user(genre_list: List[Genre], user_id: int, ascending: bool = False) -> List[
    AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesSeenByUser(genre_list, user_id, ascending)


def get_movies_of_genres_not_seen_user(genre_list: List[Genre], user_id: int, ascending: bool = False) -> List[
    AverageRating]:
    movies_from_users_favourite_genre = get_movies_by_genres(genre_list, ascending)
    users_seen_movies = get_movies_of_genres_seen_by_user(genre_list, user_id, ascending)
    return list(OrderedSet(movies_from_users_favourite_genre) - OrderedSet(users_seen_movies))


def get_count_of_movies_of_genres_not_seen_by_user(genre_list: List[Genre], user_id: int) -> int:
    return len(get_movies_of_genres_not_seen_user(genre_list, user_id))


def get_movies_by_genres(genre_list: List[Genre], ascending: bool = False) -> List[AverageRating]:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.moviesFromGenres(genre_list, ascending)


def get_average_rating_by_movie(movie_id: int) -> AverageRating:
    dao = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    output = dao.searchByMovieID(movie_id)
    if len(output) > 0:
        return output[0]
    else:
        return None


# Returns a JSON string containing the average rating of a movie
# {
#     "movie_id": 1,
#     "average_rating": "3.9"
# }
def get_average_rating(movie_id: int) -> str:
    avg_rating = get_average_rating_by_movie(movie_id)
    result_dict = {
        "movie_id": movie_id,
        "average_rating": None if avg_rating is None else "{:.2f}".format(avg_rating.getAverageRating())[:-1]
    }
    return json.dumps(result_dict, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print(get_average_rating(2))