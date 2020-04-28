from dao.generateRecommendationDAO import GenerateRecommendationDAO
from core.generateRecommendation import GenerateRecommendation
from typing import List
import constant_paths

# Returns a list of user_ids present in the table
def get_all_users() -> List[int]:
    dao = GenerateRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    result = dao.getAllUserID()
    output = []
    if len(result) != 0:
        output = [user.getUserID() for user in result]
    return output

# Returns True if an user exists by the user_id supplied
# False, otherwise
def check_user_exists(user_id: int) -> bool:
    dao = GenerateRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    user_obj = GenerateRecommendation(user_id)
    result = dao.searchByUserID(user_obj)
    return len(result) != 0


