from get_data import get_recommendation_data as grd
from get_data import get_average_rating_data as gard
from get_data import get_movie_data
from get_data import get_rating_data
from get_data import get_movie_cycle_data as gmcd
from get_data import get_link_data
from get_data import get_generating_recommendation_data as ggrd
from add_data import add_movie_cycle_data as amcd
from delete_data import delete_recommendation_data as drd
from generate_data import generateRecommendations as gr
from typing import List
import time
import json
import threading


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
# 			"imdb_id": "tt009876",
#            "tmdb_id": "7865",
# 			"title": "Max Manus (2008)"
# 			"genres": "Action, Drama, War",
# 		},
# 		{
# 			"movie_id": 170705,
# 			"imdb_id": "tt009877",
#           "tmdb_id": "7866",
# 			"title": "Band of Brothers (2001)"
# 			"genres": "Action, Drama, War",
# 		},
# 		.
# 		.
# 		.
# 	]
# }
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
                movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
                movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
                movie_temp["title"] = movie_details.getTitle()
                movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                result_dict["movies"].append(movie_temp.copy())
        else:
            result_dict["hasMovies"] = False
            result_dict["movieCount"] = 0
    else:
        result_dict["hasMovies"] = False
        result_dict["movieCount"] = 0

    return json.dumps(result_dict, indent=4, ensure_ascii=False)


# count_calls = 0
def start_generation(user_id: int):
    # global count_calls
    # count_calls += 1
    # print(f"Called {count_calls}")
    thread_name = "Thread_User_" + str(user_id)
    # Check if a thread is already running for this user
    thread_exists = False
    for thread in threading.enumerate():
        if thread.getName() == thread_name:
            print("Thread already exists! " + thread_name)
            thread_exists = True
            break
    if not thread_exists:
        x = threading.Thread(name=thread_name ,target=gr.largestIntersectionSQL, args=(user_id, True))
        x.start()


def should_generate_recommendations(user_id: int, priority: int) -> bool:
    result = None
    # Check if recommendations are already being generated
    # print(f"User {user_id} Priority {priority} exists - {ggrd.check_user_exists(user_id)}")
    if ggrd.check_user_exists(user_id):
        # If recommendations are being generated, do not spawn a thread
        result = True
    else:
        # Check if at least two of the current recommendations have unseen movies
        recommended_genres = grd.get_recommendation_data(user_id)
        if len(recommended_genres) >= 2:
            no_seen_movie_genres = []
            for genre in recommended_genres:
                genre_list = genre["common_genres"]
                if len(gard.get_movies_of_genres_not_seen_user(genre_list, user_id)) == 0:
                    no_seen_movie_genres.append(genre["priority"])
            # Delete those recommendations for which there are no unseen movies
            drd.delete_recommendations(user_id, no_seen_movie_genres)
            # If there are more than two recommendations with no unseen movies
            if len(no_seen_movie_genres) >= 2:
                start_generation(user_id)
                result = True
            else:
                result = False
        # If only one or no recommendation genre exists, start generation
        else:
            start_generation(user_id)
            result = True
    return result


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
#           "imdb_id": "tt009876",
#           "tmdb_id": "7865",
# 			"title": "Max Manus (2008)"
# 			"genres": "Action, Drama, War",
# 		},
# 		{
# 			"movie_id": 170705,
#           "imdb_id": "tt009877",
#           "tmdb_id": "7866",
# 			"title": "Band of Brothers (2001)"
# 			"genres": "Action, Drama, War",
# 		},
# 		.
# 		.
# 		.
# 	]
# }
def get_recommended_movies(user_id: int, priority: int, count: int = 15) -> str:
    # artificial_wait = 2
    # time.sleep(artificial_wait)
    result_dict = {"user_id": user_id, "priority": priority,
                   "is_generating_recommendation": should_generate_recommendations(user_id, priority)}
    # Check if new recommendations are required
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
        # elif len(movies) <= 10:
        elif len(movies) <= count:
            result_dict["hasMovies"] = True
            result_dict["movieCount"] = len(movies)
            for movie in movies:
                movie_temp = {}
                movie_id = movie.getMovieID()
                movie_details = get_movie_data.get_movie_by_id(movie_id)
                movie_temp["movie_id"] = movie_details.getMovieID()
                movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
                movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
                movie_temp["title"] = movie_details.getTitle()
                movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
                result_dict["movies"].append(movie_temp.copy())
        else:
            movie_cycle_record = gmcd.get_movie_cycle_data(user_id, priority)
            # No cycle record exists for the user
            if movie_cycle_record is None:
                # Display the first 10 movies
                # Display the first count movies
                result_dict["hasMovies"] = True
                # result_dict["movieCount"] = 10
                result_dict["movieCount"] = count
                ctr = 0
                for movie in movies:
                    # if ctr == 10:
                    if ctr == count:
                        break
                    movie_temp = {}
                    movie_id = movie.getMovieID()
                    movie_details = get_movie_data.get_movie_by_id(movie_id)
                    movie_temp["movie_id"] = movie_details.getMovieID()
                    movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
                    movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
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
                # result_dict["movieCount"] = 10
                result_dict["movieCount"] = count
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

                # ctr = 10
                ctr = count
                while ctr > 0:
                    movie_temp = {}
                    movie_id = movies[index].getMovieID()
                    movie_details = get_movie_data.get_movie_by_id(movie_id)
                    movie_temp["movie_id"] = movie_details.getMovieID()
                    movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
                    movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
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

    return json.dumps(result_dict, indent=4, ensure_ascii=False)


# Returns the top 30(default) popular unseen movies for the user
# as a JSON string as a result, and example of which is given below
# {
# 	"user_id": 1,
# 	"hasMovies": true,
#   "is_generating_recommendation": false,
# 	"movieCount": 30,
# 	"movies": [
# 		{
# 			"movie_id": 70451,
# 			"imdb_id": "tt009876",
#           "tmdb_id": "7865",
# 			"title": "Max Manus (2008)"
# 			"genres": "Action, Drama, War",
# 		},
# 		{
# 			"movie_id": 170705,
#           "imdb_id": "tt009877",
#           "tmdb_id": "7866",
# 			"title": "Band of Brothers (2001)"
# 			"genres": "Action, Drama, War",
# 		},
# 		.
# 		.
# 		.
# 	]
# }
# But, if no recommendations exist for the user, then the following JSON will be returned
# {
#     "user_id": 9,
#     "priority": 1,
#     "is_generating_recommendation": true,
#     "movies": [],
#     "hasMovies": false,
#     "movieCount": 0
# }
def get_popular_movies(user_id: int, count: int = 15) -> str:
    # Get all movies in descending order of average rating
    all_movies = gard.get_all_movies_by_average_rating(False)

    # Get movies seen by the user
    movies_seen_by_user = get_rating_data.get_movies_seen_by_user(user_id)

    # Find all movies not seen by user
    all_movie_ids = [movies.getMovieID() for movies in all_movies]
    seen_movie_ids = [movies.getMovieID() for movies in movies_seen_by_user]
    not_seen_movie_ids = list(gard.OrderedSet(all_movie_ids) - gard.OrderedSet(seen_movie_ids))

    # Create JSON string to suggest first (count) i.e. 15, etc. not seen movies
    result_dict = {"user_id": user_id, "movies": []}

    length = len(not_seen_movie_ids)

    if length < count:
        count = length

    i = 0
    while i < count:
        movie_temp = {}
        movie_id = not_seen_movie_ids[i]
        movie_details = get_movie_data.get_movie_by_id(movie_id)
        movie_temp["movie_id"] = movie_details.getMovieID()
        movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
        movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
        movie_temp["title"] = movie_details.getTitle()
        movie_temp["genres"] = movie_details.getGenres().replace('|', ', ')
        result_dict["movies"].append(movie_temp.copy())
        i += 1

    if i == 0:
        count = 0
        result_dict["hasMovies"] = False
    else:
        result_dict["hasMovies"] = True

    result_dict["movieCount"] = count

    return json.dumps(result_dict, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # print(get_all_recommended_movies(1, 3))
    user_id = 257
    print(get_recommended_movies(user_id, 1))
    # time.sleep(2)
    print(get_recommended_movies(user_id, 2))
    # time.sleep(2)
    print(get_recommended_movies(user_id, 3))
    # time.sleep(2)
    print(get_popular_movies(user_id))

    pass
