from core.tempRecommendation import TempRecommendation
from dao.tempRecommendationDAO import TempRecommendationDAO
import constant_paths


# Adds an entry to the recommendation table
def add_temp_recommendation(user_id: int, last_combination: int, priority: int, combination_num: int,
                            common_movie_length: int, genres: str):
    dao = TempRecommendationDAO(constant_paths.CONFIG_FILE_PATH)
    the_temp_recommendation = TempRecommendation(user_id, last_combination, priority, combination_num,
                                                 common_movie_length, genres)
    return dao.addTempRecommendation(the_temp_recommendation)


# Adds multiple temp recommendation entry against an user
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
def add_temp_recommendations(user_id: int, temp_recommendations: dict):
    result = True
    last_combination = temp_recommendations["last_combination"]
    for recommendation in temp_recommendations["recommendations"]:
        priority = recommendation["priority"]
        combination_num = recommendation["combination_num"]
        common_movie_length = recommendation["common_movie_length"]
        genre_ids = recommendation["common_genres"]
        genre_str = ",".join([str(x) for x in genre_ids])
        result = (result and add_temp_recommendation(user_id, last_combination, priority, combination_num,
                                                     common_movie_length, genre_str))

    # Returns True if all temp recommendations were inserted in the table
    # False otherwise
    return result


if __name__ == "__main__":
    temp_rec = {
        "last_combination": 524287,
        "recommendations": [
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
                "common_genres": [3,7,8]
            }
        ]
    }
    print(add_temp_recommendations(1, temp_rec))
