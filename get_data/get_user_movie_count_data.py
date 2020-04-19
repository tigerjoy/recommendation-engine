from core.userMovieCount import UserMovieCount
from dao.userMovieCountDAO import UserMovieCountDAO
from typing import List
import constant_paths


def get_genre_wise_movie_count_by_user(user_id: int) -> List[UserMovieCountDAO]:
    dao = UserMovieCountDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.searchByUserID(user_id)[0]