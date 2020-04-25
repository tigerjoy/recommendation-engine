from core.tempRecommendation import TempRecommendation
from dao.tempRecommendationDAO import TempRecommendationDAO
from update_data import update_temp_recommendation_data as utrd
from get_data import get_temp_recommendation as gtr
import constant_paths


# Adds an entry to the recommendation table
def add_temp_recommendation(user_id: int, last_combination: int, priority: int, combination_num: int,
                            common_movie_length: int, genres: str):
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_temp_recommendation = TempRecommendation(user_id, last_combination, priority, combination_num,
                                                 common_movie_length, genres)
    return dao.addTempRecommendation(the_temp_recommendation)


# Adds multiple temp recommendation entry against an user
# from the following example, list input and last_combination
# [
#     {
#         "priority": 1,
#         "combination_num":16,
#         "common_movie_length":11,
#         "common_genres":[5]
#     },
#     {
#         "priority": 2,
#         "combination_num":10,
#         "common_movie_length":8,
#         "common_genres":[4]
#     },
#     {
#         "priority": 3,
#         "combination_num":6,
#         "common_movie_length":4,
#         "common_genres":[3]
#     }
# ]
def add_temp_recommendations(user_id: int, last_combination: int, temp_recommendations: list):
    # print("baba")
    result = True
    #  Checking if records for user_id exists
    if len(gtr.get_temp_recommendation_by_user(user_id)) != 0:
        # print("update")
        return utrd.update_temp_recommendations(user_id, last_combination, temp_recommendations)
    else:
        for recommendation in temp_recommendations:
            priority = recommendation["priority"]
            combination_num = recommendation["combination_num"]
            common_movie_length = recommendation["common_movie_length"]
            genre_ids = recommendation["common_genres"]
            if len(genre_ids) != 0:
                genre_str = ",".join([str(x) for x in genre_ids])
            else:
                genre_str = ""
            result = (result and add_temp_recommendation(user_id, last_combination, priority, combination_num,
                                                         common_movie_length, genre_str))

        # Returns True if all temp recommendations were inserted in the table
        # False otherwise
        return result


if __name__ == "__main__":
    temp_rec = [
            {
                "priority": 1,
                "combination_num": 16,
                "common_movie_length": 11,
                "common_genres": [5]
            },
            {
                "priority": 2,
                "combination_num": 10,
                "common_movie_length": 8,
                "common_genres": [4]
            },
            {
                "priority": 3,
                "combination_num": 6,
                "common_movie_length": 4,
                "common_genres": [3,7,9]
            }
        ]
    print(add_temp_recommendations(1, 524287, temp_rec))
