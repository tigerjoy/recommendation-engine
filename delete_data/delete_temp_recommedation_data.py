from dao.tempRecommendationDAO import TempRecommendationDAO
from core.tempRecommendation import TempRecommendation
import constant_paths


def delete_temp_recommendation(user_id: int):
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_temp_recommendation = TempRecommendation(user_id)
    return dao.deleteTempRecommendation(the_temp_recommendation)