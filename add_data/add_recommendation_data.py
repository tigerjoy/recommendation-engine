from core.recommendation import Recommendation
from dao.recommendationDAO import RecommendationDAO
import constant_paths


# Adds an entry to the recommendation table
def add_recommendation(user_id: int, priority: int, genre_id: int):
    dao = RecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_recommendation = Recommendation(user_id, priority, genre_id)
    return dao.addRecommendation(the_recommendation)


# Adds multiple recommendation entry against an user
# from the following example, list input
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
def add_recommendations(user_id: int, recommendations: list):
    result = True
    for recommendation in recommendations:
        priority = recommendation["priority"]
        genre_ids = recommendation["common_genres"]
        for genre_id in genre_ids:
            result = result and add_recommendation(user_id, priority, genre_id)

    # Returns True if all recommendations were inserted in the table
    # False otherwise
    return result
