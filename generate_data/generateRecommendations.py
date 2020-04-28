import json
import time
import pprint
import constant_paths
from dao.userMovieCountDAO import UserMovieCountDAO
from typing import List
from delete_data import delete_generating_recommendation_data as dgrd
from add_data import add_temp_recommendation_data as atrd
from add_data import add_generating_recommnedation_data as agrd
from add_data import add_recommendation_data as ard
from get_data import get_average_rating_data as gard
from get_data import get_movie_data
from get_data import get_user_movie_count_data as gumcd
from get_data import get_recommendation_data as grd
from get_data import get_generating_recommendation_data as ggrd
from get_data import get_temp_recommendation as gtr
from delete_data import delete_temp_recommedation_data as dtrd
from delete_data import delete_recommendation_data as drd


# from dao.movieDAO import MovieDAO
# from dao.averageRatingDAO import AverageRatingDAO

# will be removed in iteration-3
def readJSON(filename):
    last_combination = 1
    result = []
    recommendation_dict = {"priority": 0, "combination_num": 0,
                           "common_movie_length": 0, "common_genres": []}
    for i in range(1, 4):
        recommendation_dict["priority"] = i
        result.append(recommendation_dict.copy())

    try:
        with open(filename) as json_file:
            json_string = json_file.read()
            parsed_json = json.loads(json_string)
            last_combination = parsed_json["last_combination"]
            recommendations = parsed_json["recommendations"]
            result = []
            for recommendation in recommendations:
                result.append(recommendation.copy())

    except FileNotFoundError:
        # Already assigned value above
        pass
    except:
        print("Something went wrong!")

    return last_combination, result.copy()


# will be removed in iteration-3
# Modified in iteration-3
def writeJSON(filename, last_combination, recommendation):
    with open(filename, 'w') as json_file:
        json_data = {
            'last_combination': last_combination,
            'recommendations': recommendation
        }
        json_file.write(json.dumps(json_data, indent=4))


def getTempRecommendation(user_id: int):
    result = gtr.get_temp_recommendation_by_user(user_id)

    if len(result) != 0:
        last_combination = result["last_combination"]
        recommendations = result["recommendations"]
    else:
        last_combination = 1
        recommendations = []
        recommendation_dict = {"priority": 0, "combination_num": 0,
                               "common_movie_length": 0, "common_genres": []}
        for i in range(1, 4):
            recommendation_dict["priority"] = i
            recommendations.append(recommendation_dict.copy())

    return last_combination, recommendations.copy()


def writeLog(output, filename):
    with open(filename, "a") as file:
        print(output, file=file)


def readLog(filename):
    try:
        with open(filename, "r") as file:
            for line in file.readlines():
                print(line)
    except FileNotFoundError:
        print('Output file not yet created!')
    except:
        print('Something went wrong!')


# TODO: Parallelize using multiprocessing module
# This function is with reduced genre optimization
def largestIntersectionSQL(user_id: int, verbose: bool = False):
    start_time = time.time()
    # Check if existing recommendation exists for the user
    # if so, return that recommendation
    # recommendations = grd.get_recommendation_data(user_id)
    #
    # if len(recommendations) != 0:
    #     return recommendations

    pp = pprint.PrettyPrinter(indent=4)

    filename = "log_user_{}.json".format(user_id)
    output_log_file = constant_paths.LOG_FILE_PATH + "\\" + filename[:filename.index('.')] + "_output.txt"
    valid_genres = gumcd.get_non_zero_movie_genres(user_id)

    writeLog("Non zero movie genres are", output_log_file)
    print("Non zero movie genres are")
    writeLog(valid_genres, output_log_file)
    print(valid_genres)
    start_count = 1
    # end_count = (2 ** 19)
    end_count = (2 ** len(valid_genres))

    # if verbose:
        # Read previous output if any
        # readLog(output_log_file)

    # New Addition iteration-3
    # Output
    # Read the backup file to resume processing
    # start_count, recommendations = readJSON(filename)
    start_count, recommendations = getTempRecommendation(user_id)

    # print("start_count:", start_count)
    # print("recommendations:", recommendations)

    # Starting recommendation generation
    # If the current already exists, don't add to the list
    # otherwise, add the user
    if not ggrd.check_user_exists(user_id):
        writeLog("Adding user to generating_recommendation list...", output_log_file)
        agrd.add_user(user_id)
        writeLog("done!", output_log_file)

    for count in range(start_count, end_count):
        genreList = []

        # Write the output after trying every 10,000 combinations
        if count % 10000 == 0:
            # writeJSON(filename, count, recommendations)
            # print("haha")
            atrd.add_temp_recommendations(user_id, count, recommendations)
            writeLog("Current combination {}".format(count), output_log_file)
            if verbose:
                print("Current combination {}".format(count))

        mask = 0b1000000000000000000

        # Populate the genreList
        # MSB as genre 19 and LSB as genre 1
        # genre = 19
        index = len(valid_genres) - 1
        for i in range(19):
            if count & mask:
                genreList.append(valid_genres[index])
            mask >>= 1
            # genre -= 1
            index -= 1

        # Finding the common movies falling in all the genres of the genreList
        common_movies = gard.get_movies_of_genres_seen_by_user(genreList, user_id)
        movieCount = len(common_movies)

        # New in iteration-3
        to_insert = movieCount
        j = 2
        while j >= 0:
            if to_insert > recommendations[j]["common_movie_length"]:
                # Checking if the current genre set has any unseen movies for the user
                if gard.get_count_of_movies_of_genres_not_seen_by_user(genreList, user_id) == 0:
                    break
                #   Shift elements from 0 to j - 1 one position left
                k = 0
                while k <= j - 1:
                    recommendations[k] = recommendations[k + 1].copy()
                    recommendations[k]["priority"] = k + 1
                    k += 1
                recommendations[j]["combination_num"] = count
                recommendations[j]["common_movie_length"] = movieCount
                recommendations[j]["common_genres"] = genreList.copy()
                # writeJSON(filename, count, recommendations)
                # print("\n\n", "count:", count)
                # print(recommendations)
                # print(f"atrd.add_temp_recommendations({user_id}, {count}, recommendations)\n\n")
                atrd.add_temp_recommendations(user_id, count, recommendations)
                if verbose:
                    # pp.pprint(recommendation)
                    print("The priority is {}".format(recommendations[j]["priority"]))
                    print("The combination number for the set is {}".format(recommendations[j]["combination_num"]))
                    print("The number of common movies are {}".format(recommendations[j]["common_movie_length"]))
                    print("The genre list is {}".format(recommendations[j]["common_genres"]))

                    writeLog("The priority is {}".format(recommendations[j]["priority"]), output_log_file)
                    writeLog("The combination number for the set is {}".format(recommendations[j]["combination_num"]),
                             output_log_file)
                    writeLog("The number of common movies are {}".format(recommendations[j]["common_movie_length"]),
                             output_log_file)
                    writeLog("The genre list is {}".format(recommendations[j]["common_genres"]), output_log_file)
                    print("\n\n\n")
                break
            j -= 1

    # Add the final temporary recommendations
    atrd.add_temp_recommendations(user_id, count, recommendations)

    # Delete any old recommendation
    # Continue deleting recommendations until
    # all recommendations are deleted
    writeLog("Deleting old recommendations...", output_log_file)
    print("Deleting old recommendations...")
    while not drd.delete_all_recommendations(user_id):
        pass
    writeLog("done!", output_log_file)
    print("done!")

    # Final output write
    # writeJSON(filename, count, recommendations)
    writeLog("Adding new recommendations...", output_log_file)
    print("Adding new recommendations...")
    ard.add_recommendations(user_id, recommendations)
    writeLog("done!", output_log_file)
    print("done!")

    # return combination_num, largestIntersectionMovieCount, largestIntersection
    # Ending recommendation generation
    writeLog("Deleting user from generating_recommendation list...", output_log_file)
    print("Deleting user from generating_recommendation list...")
    dgrd.delete_user(user_id)
    writeLog("done!", output_log_file)
    print("done!")

    # Cleanup of the temporary recommendations
    writeLog("Cleanup of temporary recommendations...", output_log_file)
    print("Cleanup of temporary recommendations...")
    dtrd.delete_temp_recommendation(user_id)
    writeLog("done!", output_log_file)
    print("done!")

    writeLog("The recommendations are...", output_log_file)
    print("The recommendations are...")
    json_recommendations = json.dumps(recommendations, indent=4, ensure_ascii=False)
    writeLog(json_recommendations, output_log_file)
    print(json_recommendations)
    end_time = time.time()
    time_tuple = time.gmtime(end_time - start_time)
    print("Time taken to perform intersection: {}\n\n".format(time.strftime('%H:%M:%S', time_tuple)))
    writeLog("Time taken to perform intersection: {}\n\n".format(time.strftime('%H:%M:%S', time_tuple)), output_log_file)
    return recommendations


def generateRecommendations(user_id: int, verbose: bool = False) -> None:
    start_time = time.time()
    # (combination_num, largestIntersectionMovieCount, genreList) = largestIntersectionSQL(user_id)
    recommendations = largestIntersectionSQL(user_id, verbose)
    end_time = time.time()
    time_tuple = time.gmtime(end_time - start_time)
    output_log_file = "log_user_{}_output.txt".format(user_id)
    # writeLog("The final result is", output_log_file)
    # writeLog("The final result is", output_log_file)
    # writeLog("Largest Intersection Movie Count: {}".format(largestIntersectionMovieCount), output_log_file)
    # writeLog("Genre List: {}".format(genreList), output_log_file)
    # writeLog("Time taken to perform intersection: {}".format(time.strftime('%H:%M:%S', time_tuple)), output_log_file)
    if verbose:
        print("Time taken to perform intersection: {}\n\n".format(time.strftime('%H:%M:%S', time_tuple)))
        print()
        print()
        print("The final result is")
        for recommendation in recommendations:
            print("Priority: {}".format(recommendation["priority"]))
            if "combination_num" in recommendation.keys():
                print("Combination Number: {}".format(recommendation["combination_num"]))
            if "common_movie_length" in recommendation.keys():
                print("Number of Movies Already Seen By User: {}".format(recommendation["common_movie_length"]))
            print("Genre List: {}".format(recommendation["common_genres"]))
            users_recommended_movies = gard.get_movies_of_genres_not_seen_user(
                recommendation["common_genres"], user_id, False)
            print("Number of Movies Not Seen By User: {}".format(len(users_recommended_movies)))
            print()
            count = 0
            # Displaying the movies not seen by user (only 10)
            for movie in users_recommended_movies:
                count += 1
                movie_id = movie.getMovieID()
                # print(movieDAO.searchByMovieID(movie_id)[0])
                print(get_movie_data.get_movie_by_id(movie_id))
                if count == 10:
                    break
            print("\n" * 3)

    # averageRatingDAO = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    # movieDAO = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    # movies_from_users_favourite_genre = averageRatingDAO.moviesFromGenres(genreList, False)
    # movies_from_users_favourite_genre = gard.get_movies_by_genres(genreList, False)
    # users_seen_movies = averageRatingDAO.moviesSeenByUser(genreList, user_id, False)
    # users_seen_movies = gard.get_movies_of_genres_seen_by_user(genreList, user_id, False)
    # users_recommended_movies = gard.get_movies_of_genres_not_seen_user(recommendation["common_genres"], user_id, False)
    # Displaying the movies not seen by user
    # for movie in users_recommended_movies:
    #     movie_id = movie.getMovieID()
    # print(movieDAO.searchByMovieID(movie_id)[0])
    # print(get_movie_data.get_movie_by_id(movie_id))


if __name__ == "__main__":
    user_id = int(input("Enter the user id to generate recommendations: "))
    print("Non zero movie genres are")
    print(gumcd.get_non_zero_movie_genres(user_id))
    print()
    # largestIntersectionSQL(1, True)
    generateRecommendations(user_id, True)
    # largest = largestIntersectionSQL(user_id, True)
    # print("Final output")
    # print(largest)
    # generateRecommendations(user_id)
    # for user_id in range(33, 611):
