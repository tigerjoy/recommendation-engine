from dao.recommendationDAO import RecommendationDAO
from core.recommendation import Recommendation
from get_data import get_recommendation_data as grd
from typing import List
import constant_paths


def delete_recommendation(user_id: int, priority: int) -> bool:
    dao = RecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_recommendation = Recommendation(user_id, priority)
    return dao.deleteRecommendation(the_recommendation)


# Deletes all recommendations for a user
def delete_all_recommendations(user_id: int) -> bool:
    recommendations = grd.get_recommendation_data(user_id)
    deleted_recommendations = 0
    for priority in range(1, 4):
        if delete_recommendation(user_id, priority):
            deleted_recommendations += 1

    return len(recommendations) == deleted_recommendations


# Deletes specific recommendations of a user whose priority is present in the priority list
def delete_recommendations(user_id: int, priority_list: List[int]) -> bool:
    result = True
    for priority in priority_list:
        result = result and delete_recommendation(user_id, priority_list)
    return result
