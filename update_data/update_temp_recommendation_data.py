from dao.tempRecommendationDAO import TempRecommendationDAO
from core.tempRecommendation import TempRecommendation
import constant_paths


# Updates an entry to the recommendation table
def update_temp_recommendation(user_id: int, last_combination: int, priority: int, combination_num: int,
                               common_movie_length: int, genres: str):
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_temp_recommendation = TempRecommendation(user_id, last_combination, priority, combination_num,
                                                 common_movie_length, genres)
    return dao.updateTempRecommendation(the_temp_recommendation)


# Updates multiple temp recommendation entry against an user
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
def update_temp_recommendations(user_id: int, last_combination: int, temp_recommendations: list):
    result = True
    for recommendation in temp_recommendations:
        priority = recommendation["priority"]
        combination_num = recommendation["combination_num"]
        common_movie_length = recommendation["common_movie_length"]
        genre_ids = recommendation["common_genres"]
        genre_str = ",".join([str(x) for x in genre_ids])
        result = (result and update_temp_recommendation(user_id, last_combination, priority, combination_num,
                                                        common_movie_length, genre_str))

    # Returns True if all temp recommendations were inserted in the table
    # False otherwise
    return result
