# from dao.ratingDAO import RatingDAO
# from dao.movieGenreDAO import MovieGenreDAO
# from dao.movieDAO import MovieDAO
#
# ratingDAO = RatingDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")
# movieGenreDAO = MovieGenreDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")
# movieDAO = MovieDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")
#
# user1_movies = ratings[ratings["userId"] == 1]["movieId"]
# List of Rating objects
# user1_ratings = ratingDAO.searchByUserID(1)
#
# user1_movie_gen = movie_gen.loc[movie_gen["movieId"].isin(user1_movies)]
# List of MovieGenre objects
# user1_movie_genres = movieGenreDAO.searchByUserRatingList(user1_ratings)
#
# genreList = [ 1 ]
#
# userMovieList is also known as user1_movie_genres
# movies_of_genre = userMovieList.loc[userMovieList[genreIdColName] == genreList[0]]
# seen_movies_of_genreList =
#
# What movies has user 1 seen for genre 1

# Assumption that there are no negative
# negative numbers in the array

# arr = [38, 41, 18, 50, 68, 22, 34]

# the first index is the third largest
# second index is the second largest
# third index is the largest
# largest = [0, 0, 0]
#
# i = 0
# size = len(arr)
# while i < size:
#     to_insert = arr[i]
#     j = 2
#     while j >= 0:
#         if to_insert > largest[j]:
            #   Shift elements from 0 to j - 1 one position left
#             k = 0
#             while k <= j - 1:
#                 largest[k] = largest[k + 1]
#                 k += 1
#             largest[j] = to_insert
#             break
#         j -= 1
#     i += 1
#
# print(largest)

# New Addition iteration-3
recommendation_dict = {"priority": 0, "combination_num": 0,
                       "common_movie_length": 0, "common_genres": []}
largest_3 = []
for i in range(1, 4):
    recommendation_dict["priority"] = i
    largest_3.append(recommendation_dict.copy())

print(largest_3)