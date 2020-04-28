from dao.userMovieCountDAO import UserMovieCountDAO
from core.userMovieCount import UserMovieCount
from get_data import get_user_movie_count_data as gumcd
from typing import List
import constant_paths


# Updates the entry for user with user_id and for
# genres present in the genre list by 1
# genreList is a list of genreIds
def update_count(userId: int, genreList: List[int]):
    dao = UserMovieCountDAO(constant_paths.CONFIG_FILE_PATH)
    # Retrieve the existing entry for user
    user_movie_count = gumcd.get_genre_wise_movie_count_by_user(userId)
    # Increment the count of those genres in user_movie_count
    # which are present in genreList
    for genreId in genreList:
        index = genreId - 1
        user_movie_count.getGenreCount()[index] += 1
    # Update the record
    return dao.updateMovieGenreCount(user_movie_count)
