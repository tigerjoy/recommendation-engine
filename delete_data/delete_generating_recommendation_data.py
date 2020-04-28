from dao.generateRecommendationDAO import GenerateRecommendationDAO
from core.generateRecommendation import GenerateRecommendation
from typing import List
import constant_paths

# To delete the user entry from table
def delete_user(user_id: int) -> bool:
    dao = GenerateRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_user = GenerateRecommendation(user_id)
    return dao.deleteUserID(the_user)
