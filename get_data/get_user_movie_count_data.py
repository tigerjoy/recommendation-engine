from core.userMovieCount import UserMovieCount
from dao.userMovieCountDAO import UserMovieCountDAO
from typing import List
import constant_paths


def get_genre_wise_movie_count_by_user(user_id: int) -> UserMovieCount:
    dao = UserMovieCountDAO(constant_paths.CONFIG_FILE_PATH)
    output = dao.searchByUserID(user_id)
    if len(output) > 0:
        return output[0]
    else:
        return None


def get_non_zero_movie_genres(user_id: int) -> List[int]:
    genre_info = get_genre_wise_movie_count_by_user(user_id)
    genre_list = []
    genre_id = 1
    for genre_count in genre_info.genreCounts:
        if genre_count > 0:
            genre_list.append(genre_id)
        genre_id += 1
    return genre_list.copy()


