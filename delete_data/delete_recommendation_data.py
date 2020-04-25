from dao.recommendationDAO import RecommendationDAO
from core.recommendation import Recommendation
import constant_paths


def delete_recommendation(user_id: int, priority: int):
    dao = RecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_recommendation = Recommendation(user_id, priority)
    return dao.deleteRecommendation(the_recommendation)