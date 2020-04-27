from get_data import get_recommendation_data as grd
from get_data import get_average_rating_data as gard
from get_data import get_movie_data
from get_data import get_movie_cycle_data as gmcd
from add_data import add_movie_cycle_data as amcd
import json


# Returns all the recommended movies for user_id for a
# particular priority as a JSON string, an example is provided below
# The JSON string is indented by 4 spaces
# {
# 	"user_id": 1,
# 	"priority": 3,
#   "hasMovies": true,
#   "movieCount" : 41,
# 	"movies": [
# 		{
# 			"movie_id": 70451,
# 			"title": "Max Manus (2008)"
# 			"genres": "Action, Drama, War",
# 		},
# 		{
# 			"movie_id": 170705,
# 			"title": "Band of Brothers (2001)"
# 			"genres": "Action, Drama, War",
# 		},
# 		.
# 		.
# 		.
# 	]
# }
# TODO: Add IMDB id for movieId
def get_all_recommended_movies(user_id: int, priority: int) -> str:
    result_dict = {"user_id": user_id, "priority": priority}
    recommended_genres = grd.get_recommendation_data(user_id)
    genre_list = []
    for recommend_genre in recommended_genres:
        if recommend_genre["priority"] == priority:
            genre_list = recommend_genre["common_genres"]
            break
    result_dict["movies"] = []
    if len(genre_list) != 0:
        movies = gard.get_movies_of_genres_not_seen_user(genre_list, user_id)
        if len(movies) != 0:
            result_dict["hasMovies"] = True
            result_dict["movieCount"] = len(movies)
            for movie in movies:
                movie_temp = {}
                movie_id = movie.getMovieID()
                movie_details = get_movie_data.get_movie_by_id(movie_id)
                movie_temp["movie_id"] = movie_details.getMovieID()
                movie_temp["title"] = movie_details.getTitle()
                movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                result_dict["movies"].append(movie_temp.copy())
        else:
            result_dict["hasMovies"] = False
            result_dict["movieCount"] = 0
    else:
        result_dict["hasMovies"] = False
        result_dict["movieCount"] = 0

    return json.dumps(result_dict, indent=4)


# Returns 10 recommended movies at a time for user_id for a
# particular priority as a JSON string, an example is provided below
# The JSON string is indented by 4 spaces
# {
# 	"user_id": 1,
# 	"priority": 3,
#   "hasMovies": true,
#   "movieCount" : 10,
# 	"movies": [
# 		{
# 			"movie_id": 70451,
# 			"title": "Max Manus (2008)"
# 			"genres": "Action, Drama, War",
# 		},
# 		{
# 			"movie_id": 170705,
# 			"title": "Band of Brothers (2001)"
# 			"genres": "Action, Drama, War",
# 		},
# 		.
# 		.
# 		.
# 	]
# }
def get_recommended_movies(user_id: int, priority: int) -> str:
    result_dict = {"user_id": user_id, "priority": priority}
    recommended_genres = grd.get_recommendation_data(user_id)
    genre_list = []
    for recommend_genre in recommended_genres:
        if recommend_genre["priority"] == priority:
            genre_list = recommend_genre["common_genres"]
            break
    result_dict["movies"] = []
    if len(genre_list) != 0:
        movies = gard.get_movies_of_genres_not_seen_user(genre_list, user_id)
        if len(movies) == 0:
            result_dict["hasMovies"] = False
            result_dict["movieCount"] = 0
        elif len(movies) <= 10:
            result_dict["hasMovies"] = True
            result_dict["movieCount"] = len(movies)
            for movie in movies:
                movie_temp = {}
                movie_id = movie.getMovieID()
                movie_details = get_movie_data.get_movie_by_id(movie_id)
                movie_temp["movie_id"] = movie_details.getMovieID()
                movie_temp["title"] = movie_details.getTitle()
                movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                result_dict["movies"].append(movie_temp.copy())
        else:
            movie_cycle_record = gmcd.get_movie_cycle_data(user_id, priority)
            # No cycle record exists for the user
            if movie_cycle_record is None:
                # Display the first 10 movies
                result_dict["hasMovies"] = True
                result_dict["movieCount"] = 10
                ctr = 0
                for movie in movies:
                    if ctr == 10:
                        break
                    movie_temp = {}
                    movie_id = movie.getMovieID()
                    movie_details = get_movie_data.get_movie_by_id(movie_id)
                    movie_temp["movie_id"] = movie_details.getMovieID()
                    movie_temp["title"] = movie_details.getTitle()
                    movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                    result_dict["movies"].append(movie_temp.copy())
                    ctr += 1
                last_movie_id = result_dict["movies"][9]["movie_id"]
                second_last_movie_id = result_dict["movies"][8]["movie_id"]
            else:
                last_movie_id = movie_cycle_record.getLastMovieID()
                second_last_movie_id = movie_cycle_record.getSecondLastMovieID()
                # print("last_movie_id:", last_movie_id)
                # print("second_last_movie_id", second_last_movie_id)
                result_dict["hasMovies"] = True
                result_dict["movieCount"] = 10
                last_movie_index = -1
                second_last_movie_index = -1
                movies_length = len(movies)
                i = 0
                for movie in movies:
                    # print(movie)
                    if movie.getMovieID() == last_movie_id:
                        last_movie_index = i
                    else:
                        pass
                    if movie.getMovieID() == second_last_movie_id:
                        second_last_movie_index = i
                    else:
                        pass
                    if last_movie_index != -1 and second_last_movie_index != -1:
                        break
                    i += 1

                # print("i:", i)
                # print("last_movie_index:", last_movie_index)
                # print("second_last_movie_index", second_last_movie_index)

                if last_movie_index != -1:
                    index = (last_movie_index + 1) % movies_length
                else:
                    index = (second_last_movie_index + 1) % movies_length

                ctr = 10
                while ctr > 0:
                    movie_temp = {}
                    movie_id = movies[index].getMovieID()
                    movie_details = get_movie_data.get_movie_by_id(movie_id)
                    movie_temp["movie_id"] = movie_details.getMovieID()
                    movie_temp["title"] = movie_details.getTitle()
                    movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                    result_dict["movies"].append(movie_temp.copy())
                    ctr -= 1
                    index = (index + 1) % movies_length

                last_movie_id = result_dict["movies"][9]["movie_id"]
                second_last_movie_id = result_dict["movies"][8]["movie_id"]

            amcd.add_movie_cycle_data(user_id, last_movie_id, second_last_movie_id, priority)
    else:
        result_dict["hasMovies"] = False
        result_dict["movieCount"] = 0

    return json.dumps(result_dict, indent=4)


if __name__ == "__main__":
    # print(get_all_recommended_movies(1, 3))
    # print(get_recommended_movies(1, 3))
    pass