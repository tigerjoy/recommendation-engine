from core.rating import Rating
from dao.ratingDAO import RatingDAO
from typing import List
import constant_paths
import json


# Added get_rating_by_user_movie() to retrieve the rating against a user_id and movie_id
def get_rating_by_user_movie(user_id: int, movie_id: int) -> Rating:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    output = dao.searchByUserIDMovieID(user_id, movie_id)
    if len(output) > 0:
        return output[0]
    else:
        return None


# To get_average_rating_by_id() to calculate the current average rating of a movie
def get_average_rating_by_movie(movie_id: int) -> float:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.calculateAverageRatingByMovie(movie_id)


# To get movie_id and rating information of movies seen by user
def get_movies_seen_by_user(user_id: int) -> List[Rating]:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.searchByUserID(user_id)


# Returns a JSON string containing the rating of a movie given by a user
# {
#     "user_id": 1,
#     "movie_id": 1,
#     "rating": "3.9"
# }
def get_rating_data(user_id: int, movie_id: int) -> str:
    rating = get_rating_by_user_movie(user_id, movie_id)
    result_dict = {
        "user_id": user_id,
        "movie_id": movie_id,
        "rating": None if rating is None else "{:.2f}".format(rating.getRating())[:-1]
    }
    return json.dumps(result_dict, indent=4, ensure_ascii=False)


# Returns a JSON string containing the user_ids of all users
# {
#     "user_ids": [
#         1, 2, 3, 4, 6, ....
#     ]
# }
def get_all_users() -> str:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    user_ids = dao.getAllUsers()
    result_dict = {"user_ids": []}
    for user_id in user_ids:
        result_dict["user_ids"].append(user_id)
    return json.dumps(result_dict, indent=4, ensure_ascii=False)


# Returns a JSON string containing the result of checking if a
# user exists
# {
#     "user_id": 1,
#     "exist: true
# }
def check_user_exists(userId: int) -> str:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    user_ids = dao.getAllUsers()
    result_dict = {"user_id": userId, "exist": False}
    for user_id in user_ids:
        if user_id == userId:
            result_dict["exist"] = True
            break
    return json.dumps(result_dict, indent=4, ensure_ascii=False)


# Returns a JSON string containing true if user_id has watched movie_id
# false, otherwise
# {
#     "user_id": 1,
#     "movie_id": 1,
#     "has_watched": true
# }
def has_watched(user_id: int, movie_id: int) -> str:
    rating = get_rating_by_user_movie(user_id, movie_id)
    result_dict = {
        "user_id": user_id,
        "movie_id": movie_id,
        "has_watched": rating is not None
    }
    return json.dumps(result_dict, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print(has_watched(1, 2))
