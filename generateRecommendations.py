import json
from dao.ratingDAO import RatingDAO

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

def largestIntersectionV3(userMovieList, genreIdColName, movieIdColName, filename=None):
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
                set(userMovieList[userMovieList[movieIdColName].isin(movieIds) & (userMovieList[genreIdColName] != genreList[0])][movieIdColName].unique()))
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
    pass