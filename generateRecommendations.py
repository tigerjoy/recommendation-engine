import json
import time
import pprint
import createConfig
import constant_paths
from dao.movieDAO import MovieDAO
from dao.averageRatingDAO import AverageRatingDAO


def readJSON(filename):
    last_combination = 1
    combination_num = 0
    common_movie_length = 0
    common_genres = []

    try:
        with open(filename) as json_file:
            json_string = json_file.read()
            parsed_json = json.loads(json_string)
            combination_num = parsed_json['combination_num']
            common_movie_length = parsed_json['common_movie_length']
            common_genres = parsed_json['common_genres']
            last_combination = parsed_json["last_combination"]
    except FileNotFoundError:
        # Already assigned value above
        pass
    except:
        print("Something went wrong!")

    return last_combination, combination_num, common_movie_length, common_genres


# Modified in iteration-3
def writeJSON(filename, last_combination, recommendation):
    with open(filename, 'w') as json_file:
        json_data = {
            'last_combination': last_combination,
            'recommendation': recommendation
        }
        json_file.write(json.dumps(json_data, indent=4))


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


# TODO: Implement reduction of genre choices by removing genres
# TODO: Output three sets of genre list, largest, second largest, third largest
# TODO: Parallelize using multiprocessing module
# This function is without any optimization
def largestIntersectionSQL(user_id: int, verbose: bool = False):
    pp = pprint.PrettyPrinter(indent=4)
    filename = "log_user_{}.json".format(user_id)
    output_log_file = filename[:filename.index('.')] + "_output.txt"
    start_count = 1
    end_count = (2 ** 19)

    # if verbose:
    # Read previous output if any
    # readLog(output_log_file)

    # Output
    # combination_num = 0
    # largestIntersectionMovieCount = 0
    # largestIntersection = []

    # Read the backup file to resume processing
    # if filename is not None:
    #     start_count, combination_num, largestIntersectionMovieCount, largestIntersection = readJSON(filename)

    # New Addition iteration-3
    recommendation_dict = {"priority": 0, "combination_num": 0,
                           "common_movie_length": 0, "common_genres": []}
    recommendation = []
    for i in range(1, 4):
        recommendation_dict["priority"] = i
        recommendation.append(recommendation_dict.copy())

    for count in range(start_count, end_count):
        genreList = []

        # Write the output after trying every 10,000 combinations
        if count % 10000 == 0:
            writeJSON(filename, count, recommendation)
            writeLog("Current combination {}".format(count), output_log_file)
            if verbose:
                print("Current combination {}".format(count))

        mask = 0b1000000000000000000

        # Populate the genreList
        # MSB as genre 19 and LSB as genre 1
        genre = 19
        for i in range(19):
            if count & mask:
                genreList.append(genre)
            mask >>= 1
            genre -= 1

        averageRatingDAO = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
        # Finding the common movies falling in all the genres of the genreList
        common_movies = averageRatingDAO.moviesSeenByUser(genreList, user_id)
        movieCount = len(common_movies)

        # New in iteration-3
        to_insert = movieCount
        j = 2
        while j >= 0:
            if to_insert > recommendation[j]["common_movie_length"]:
                #   Shift elements from 0 to j - 1 one position left
                k = 0
                while k <= j - 1:
                    recommendation[k] = recommendation[k + 1].copy()
                    recommendation[k]["priority"] = k + 1
                    k += 1
                # largest[j] = to_insert
                recommendation[j]["combination_num"] = count
                recommendation[j]["common_movie_length"] = movieCount
                recommendation[j]["common_genres"] = genreList.copy()
                writeJSON(filename, count, recommendation)
                if verbose:
                    # pp.pprint(recommendation)
                    print("The priority is {}".format(recommendation[j]["priority"]))
                    print("The combination number for the set is {}".format(recommendation[j]["combination_num"]))
                    print("The number of common movies are {}".format(recommendation[j]["common_movie_length"]))
                    print("The genre list is {}".format(recommendation[j]["common_genres"]))

                    writeLog("The priority is {}".format(recommendation[j]["priority"]), output_log_file)
                    writeLog("The combination number for the set is {}".format(recommendation[j]["combination_num"]),
                             output_log_file)
                    writeLog("The number of common movies are {}".format(recommendation[j]["common_movie_length"]),
                             output_log_file)
                    writeLog("The genre list is {}".format(recommendation[j]["common_genres"]), output_log_file)
                    print("\n\n\n")
                break
            j -= 1

        # Will be removed in iteration-3
        # if movieCount > largestIntersectionMovieCount:
        #     largestIntersection = genreList.copy()
        #     largestIntersectionMovieCount = movieCount
        #     combination_num = count
        #     writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
        #     writeLog("The combination number for the set is {}".format(combination_num), output_log_file)
        #     writeLog("The number of common movies are {}".format(largestIntersectionMovieCount), output_log_file)
        #     writeLog("The genre list is {}".format(genreList), output_log_file)
        #     if verbose:
        #         print("The combination number for the set is {}".format(combination_num))
        #         print("The number of common movies are {}".format(largestIntersectionMovieCount))
        #         print("The genre list is {}".format(genreList))

    # Final output write
    writeJSON(filename, count, recommendation)
    # return combination_num, largestIntersectionMovieCount, largestIntersection
    return recommendation


def generateRecommendations(user_id: int, verbose: bool = False) -> None:
    start_time = time.time()
    (combination_num, largestIntersectionMovieCount, genreList) = largestIntersectionSQL(user_id)
    end_time = time.time()
    time_tuple = time.gmtime(end_time - start_time)
    output_log_file = "log_user_{}_output.txt".format(user_id)
    writeLog("The final result is", output_log_file)
    writeLog("The final result is", output_log_file)
    writeLog("Largest Intersection Movie Count: {}".format(largestIntersectionMovieCount), output_log_file)
    writeLog("Genre List: {}".format(genreList), output_log_file)
    writeLog("Time taken to perform intersection: {}".format(time.strftime('%H:%M:%S', time_tuple)), output_log_file)
    if verbose:
        print("The final result is")
        print("Combination Number: {}".format(combination_num))
        print("Largest Intersection Movie Count: {}".format(largestIntersectionMovieCount))
        print("Genre List: {}".format(genreList))
        print("Time taken to perform intersection: {}\n\n".format(time.strftime('%H:%M:%S', time_tuple)))

    averageRatingDAO = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    movieDAO = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    movies_from_users_favourite_genre = averageRatingDAO.moviesFromGenres(genreList, False)
    users_seen_movies = averageRatingDAO.moviesSeenByUser(genreList, user_id, False)
    users_recommended_movies = set(movies_from_users_favourite_genre).difference(users_seen_movies)
    # Displaying the movies not seen by user
    for movie in users_recommended_movies:
        movie_id = movie.getMovieID()
        print(movieDAO.searchByMovieID(movie_id)[0])


if __name__ == "__main__":
    user_id = int(input("Enter the user id to generate recommendations: "))
    largest = largestIntersectionSQL(1, True)
    print("Final output")
    print(largest)
    # generateRecommendations(user_id)
    # for user_id in range(33, 611):
