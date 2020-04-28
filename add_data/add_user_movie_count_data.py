from dao.userMovieCountDAO import UserMovieCountDAO
from core.userMovieCount import UserMovieCount
from get_data import get_user_movie_count_data as gumcd
from update_data import update_user_movie_count_data as uumc
from typing import List
import constant_paths


# Adds the entry for user with user_id and for
# genres present in the genreList
def add_count(userId: int, genreList: List[int]):
    dao = UserMovieCountDAO(constant_paths.CONFIG_FILE_PATH)
    # Check if there is an existing record
    if gumcd.get_genre_wise_movie_count_by_user(userId) is not None:
        return uumc.update_count(userId, genreList)
    else:
        # Create the object
        user_movie_count = UserMovieCount(userId)
        for genreId in genreList:
            index = genreId - 1
            user_movie_count.getGenreCount()[index] += 1
        # Add the record
        return dao.addUserMovieGenreCount(user_movie_count)