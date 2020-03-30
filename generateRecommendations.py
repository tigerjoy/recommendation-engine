import json
import time
import constant_paths
from dao.movieDAO import MovieDAO
from dao.averageRatingDAO import AverageRatingDAO


# TODO: Implement error handling for non-existing log files for the first run
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


def writeJSON(filename, last_combination, combination_num, common_movie_length, common_genres):
    with open(filename, 'w') as json_file:
        json_data = {
            'last_combination': last_combination,
            'combination_num': combination_num,
            'common_movie_length': common_movie_length,
            'common_genres': common_genres
        }
        json_file.write(json.dumps(json_data))


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
def largestIntersectionSQL(user_id: int):
    filename = "log_user_{}.json".format(user_id)
    output_log_file = filename[:filename.index('.')] + "_output.txt"
    start_count = 1
    end_count = (2 ** 19)

    # Read previous output if any
    readLog(output_log_file)

    # Output
    combination_num = 0
    largestIntersectionMovieCount = 0
    largestIntersection = []

    # Read the backup file to resume processing
    if filename is not None:
        start_count, combination_num, largestIntersectionMovieCount, largestIntersection = readJSON(filename)

    for count in range(start_count, end_count):
        genreList = []

        # Write the output after trying every 10,000 combinations
        if count % 10000 == 0:
            writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
            writeLog("Current combination {}".format(count), output_log_file)
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
        if movieCount > largestIntersectionMovieCount:
            largestIntersection = genreList.copy()
            largestIntersectionMovieCount = movieCount
            combination_num = count
            writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
            print("The combination number for the set is {}".format(combination_num))
            writeLog("The combination number for the set is {}".format(combination_num), output_log_file)
            print("The number of common movies are {}".format(largestIntersectionMovieCount))
            writeLog("The number of common movies are {}".format(largestIntersectionMovieCount), output_log_file)
            print("The genre list is {}".format(genreList))
            writeLog("The genre list is {}".format(genreList), output_log_file)

    # Final output
    writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
    return combination_num, largestIntersectionMovieCount, largestIntersection

def generateRecommendations(user_id: int) -> None:
    start_time = time.time()
    (combination_num, largestIntersectionMovieCount, genreList) = largestIntersectionSQL(1)
    output_log_file = "log_user_{}_output.txt".format(user_id)

    print("The final result is")
    writeLog("The final result is", output_log_file)
    print("Combination Number: {}".format(combination_num))
    writeLog("The final result is", output_log_file)
    print("Largest Intersection Movie Count: {}".format(largestIntersectionMovieCount))
    writeLog("Largest Intersection Movie Count: {}".format(largestIntersectionMovieCount), output_log_file)
    print("Genre List: {}".format(genreList))
    writeLog("Genre List: {}".format(genreList), output_log_file)
    end_time = time.time()
    time_tuple = time.gmtime(end_time - start_time)
    print("Time taken to perform intersection: {}\n\n".format(time.strftime('%H:%M:%S', time_tuple)))
    writeLog("Time taken to perform intersection: {}".format(time.strftime('%H:%M:%S', time_tuple)), output_log_file)

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
    generateRecommendations(user_id)
    # for user_id in range(33, 611):

