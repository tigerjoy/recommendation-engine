from dao.ratingDAO import RatingDAO
from dao.movieGenreDAO import MovieGenreDAO
from dao.movieDAO import MovieDAO

ratingDAO = RatingDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")
movieGenreDAO = MovieGenreDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")
movieDAO = MovieDAO("C:\\Users\\Ranajoy\\PycharmProjects\\recommendation-engine\\config\\db_properties.json")

# user1_movies = ratings[ratings["userId"] == 1]["movieId"]
# List of Rating objects
user1_ratings = ratingDAO.searchByUserID(1)

# user1_movie_gen = movie_gen.loc[movie_gen["movieId"].isin(user1_movies)]
# List of MovieGenre objects
user1_movie_genres = movieGenreDAO.searchByUserRatingList(user1_ratings)

genreList = [ 1 ]

# userMovieList is also known as user1_movie_genres
# movies_of_genre = userMovieList.loc[userMovieList[genreIdColName] == genreList[0]]
# seen_movies_of_genreList =

# What movies has user 1 seen for genre 1
