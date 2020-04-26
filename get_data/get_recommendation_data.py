from core.recommendation import Recommendation
from dao.recommendationDAO import RecommendationDAO
from typing import List
import constant_paths


# Returns multiple recommendation entry against an user
# from the following example, list output
# [
#     {
#         "priority": 1,
#         "common_genres":[5, 9]
#     },
#     {
#         "priority": 2,
#         "common_genres":[4]
#     },
#     {
#         "priority": 3,
#         "common_genres":[3]
#     }
# ]
def get_recommendation_data(user_id: int) -> List[dict]:
    dao = RecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    recommendation_list = dao.getRecommendationByUser(user_id)
    recommendations = []
    for priority in range(1, 4):
        result_dict = {"priority": priority}
        genre_list = []
        for recommendation in recommendation_list:
            if recommendation.getPriority() == priority:
                genre_list.append(int(recommendation.getGenreID()))
        result_dict["common_genres"] = genre_list.copy()
        if len(result_dict["common_genres"]) != 0:
            recommendations.append(result_dict.copy())
    return recommendations
