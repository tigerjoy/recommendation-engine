import json
import constant_paths
from dao.movieDAO import MovieDAO
from dao.ratingDAO import RatingDAO
from dao.movieGenreDAO import MovieGenreDAO
from dao.averageRatingDAO import AverageRatingDAO


# TODO: Implement error handling for non-existing log files for the first run
def readJSON(filename):
    with open(filename) as json_file:
        json_string = json_file.read()
        if json_string == "":
            last_combination = 0
            combination_num = 0
            common_movie_length = 0
            common_genres = []
        else:
            parsed_json = json.loads(json_string)
            combination_num = parsed_json['combination_num']
            common_movie_length = parsed_json['common_movie_length']
            common_genres = parsed_json['common_genres']
            last_combination = parsed_json["last_combination"]
    return (last_combination, combination_num, common_movie_length, common_genres)


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
        print(output, file=filename)


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
    filename = "log_user_{}".format(user_id)
    # TODO: Remove the next three lines after finishing this function
    userMovieList = None
    genreIdColName = None
    movieIdColName = None

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
    if filename != None:
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

        # Finding the common movies falling in all the genres of the genreList
        common_movies = set({})
        if len(genreList) == 1:
            # Implement logic of how to fetch movieIds / MovieGenre obj list
            # for movies belonging only to 1 genre say seen by user, only Action movies
            movies_of_genre = userMovieList.loc[userMovieList[genreIdColName] == genreList[0]]
            movieIds = movies_of_genre["movieId"]
            common_movies = set(movieIds).difference(
                set(userMovieList[
                        userMovieList[movieIdColName].isin(movieIds) & (userMovieList[genreIdColName] != genreList[0])][
                        movieIdColName].unique()))
        elif len(genreList) != 0:
            # logic already implemented searchByGenreID()
            common_movies = set(userMovieList.loc[
                                    userMovieList[genreIdColName] == genreList[0]
                                    ][movieIdColName])

        for index in range(1, len(genreList)):
            common_movies = common_movies.intersection(set(
                userMovieList.loc[
                    userMovieList[genreIdColName] == genreList[index]
                    ][movieIdColName]))

        # Finding if the current genreList has the highest number of common movies
        movieCount = len(common_movies)
        if movieCount > largestIntersectionMovieCount:
            largestIntersection = genreList.copy()
            largestIntersectionMovieCount = movieCount
            combination_num = count
            writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
            print("The combination number for the set is {}".format(combination_num))
            print("The number of common movies are {}".format(largestIntersectionMovieCount))
            print("The genre list is {}".format(genreList))


def largestIntersectionV3(userMovieList, genreIdColName, movieIdColName, filename=None):
    # No need to change the below lines
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
    if filename != None:
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

        # Finding the common movies falling in all the genres of the genreList
        common_movies = set({})
        if len(genreList) == 1:
            movies_of_genre = userMovieList.loc[userMovieList[genreIdColName] == genreList[0]]
            movieIds = movies_of_genre["movieId"]
            common_movies = set(movieIds).difference(
                set(userMovieList[
                        userMovieList[movieIdColName].isin(movieIds) & (userMovieList[genreIdColName] != genreList[0])][
                        movieIdColName].unique()))
        elif len(genreList) != 0:
            common_movies = set(userMovieList.loc[
                                    userMovieList[genreIdColName] == genreList[0]
                                    ][movieIdColName])

        for index in range(1, len(genreList)):
            common_movies = common_movies.intersection(set(
                userMovieList.loc[
                    userMovieList[genreIdColName] == genreList[index]
                    ][movieIdColName]))

        # Finding if the current genreList has the highest number of common movies
        movieCount = len(common_movies)
        if movieCount > largestIntersectionMovieCount:
            largestIntersection = genreList.copy()
            largestIntersectionMovieCount = movieCount
            combination_num = count
            writeJSON(filename, count, combination_num, largestIntersectionMovieCount, largestIntersection)
            print("The combination number for the set is {}".format(combination_num))
            print("The number of common movies are {}".format(largestIntersectionMovieCount))
            print("The genre list is {}".format(genreList))
    return (combination_num, largestIntersectionMovieCount, largestIntersection)


if __name__ == "__main__":
    ratingDAO = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    movieGenreDAO = MovieGenreDAO(constant_paths.CONFIG_FILE_PATH)
    averageRatingDAO = AverageRatingDAO(constant_paths.CONFIG_FILE_PATH)
    movieDAO = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    # Start Time
    # No changes to below line
    # start_time = time.time()

    # user1_movies = ratings[ratings["userId"] == 1]["movieId"]
    user1_ratings = ratingDAO.searchByUserID(1)
    # To select only those rows where movieId belongs to user1_movies
    # user1_movie_gen = movie_gen.loc[movie_gen["movieId"].isin(user1_movies)]
    user1_movie_genre = movieGenreDAO.searchByUserRatingList(user1_ratings)

    # No change (maybe some change)
    # Calling the method to perform intersection
    # (combination_num, largestIntersectionMovieCount, genreList) = largestIntersectionV3(user1_movie_gen, "genreId",
    #                                                                                       "movieId", "log.json")

    # End Time
    # No changes to below line
    # end_time = time.time()

    # No changes to below lines
    # time_tuple = time.gmtime(end_time - start_time)
    # print("Time taken to perform intersection: {}".format(time.strftime('%H:%M:%S', time_tuple)))

    # Below lines for reference
    # average_rating = pd.read_csv(
    #     "/content/drive/My Drive/Research Papers & Useful Links to Datasets/Preprocessed Dataset/average-rating.csv")

    # movie_gen.loc[movie_gen["genreId"] == 1]
    # movieGenreDAO.searchByGenreID(1)

    # merged_df = average_rating.merge(movie_gen.loc[(movie_gen["genreId"] == 2) & (movie_gen["genreId"] == 1)],
    #                                                                                   on="movieId", how="inner")
    movies_from_user1_favourite_genre = averageRatingDAO.selectFromJoin([1, 2], False)
    user1_seen_movies = averageRatingDAO.moviesSeenByUser([1, 2], 1, False)
    user1_recommended_movies = set(movies_from_user1_favourite_genre).difference(user1_seen_movies)
    # Displaying the movies not seen by user1
    for movie in user1_recommended_movies:
        movie_id = movie.getMovieID()
        print(movieDAO.searchByMovieID(movie_id)[0])
    # SELECT movie_gen.movieId, avgRating, genreId
    # FROM average_rating INNER JOIN ON average_rating.movieId = movie_gen.movieId
    # WHERE genreId = 1;
    # Return format:
    # JSON
    # {
    #     "1":{
    #         "genres": [2, 3, 4, 5, 9], ( Dont Need the Genre)
    #         "avgRating": 3.92093023255814
    #     }
    # }
    # OR
    # Simple Object List is better as we dont need the genre,
    # The genre information is already available to us

    # highestRated = merged_df.sort_values("avgRating", ascending=False)

    # Below lines for reference
    # movies = pd.read_csv(
    #     "/content/drive/My Drive/Research Papers & Useful Links to Datasets/Preprocessed Dataset/movies_out.csv")

    # highestRated.head(20).merge(movies, on="movieId", how="inner")

    # for i in range(20):
    #     print(movieDAO.searchByMovieID()[0])
