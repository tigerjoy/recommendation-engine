from core.tempRecommendation import TempRecommendation
from dao.tempRecommendationDAO import TempRecommendationDAO
from typing import List
import pprint
import constant_paths


# Returns multiple temp recommendation entry against an user
# from the following example, dictionary input
# {
#     "last_combination": 524287,
#     "recommendations": [
#         {
#             "priority": 1,
#             "combination_num":16,
#             "common_movie_length":11,
#             "common_genres":[5]
#         },
#         {
#             "priority": 2,
#             "combination_num":10,
#             "common_movie_length":8,
#             "common_genres":[4]
#         },
#         {
#             "priority": 3,
#             "combination_num":6,
#             "common_movie_length":4,
#             "common_genres":[3]
#         }
#     ]
# }
def get_temp_recommendation_by_user(user_id: int) -> dict:
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    temp_reco_list = dao.getTempRecommendationByUserID(user_id)
    # print("temp_reco_list: ", temp_reco_list)
    last_combination = None
    result = {}
    recommendations = []
    for temp_reco in temp_reco_list:
        last_combination = temp_reco.getLastCombination()
        priority = temp_reco.getPriority()
        combination_num = temp_reco.getCombinationNum()
        common_movie_length = temp_reco.getCommonMovieLength()
        genres = temp_reco.getGenres()
        if len(genres) == 0:
            common_genres = []
        else:
            common_genres = [int(x) for x in genres.split(",")]
        reco_dict = {"priority": priority, "combination_num": combination_num,
                     "common_movie_length": common_movie_length, "common_genres": common_genres.copy()}
        recommendations.append(reco_dict.copy())

    if last_combination is not None:
        result["recommendations"] = recommendations.copy()
        result["last_combination"] = last_combination

    return result


def get_all_user_id():
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.getAllUserID()


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(get_temp_recommendation_by_user(1))
