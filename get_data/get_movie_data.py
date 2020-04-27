from core.movie import Movie
from dao.movieDAO import MovieDAO
from typing import List
from get_data import get_link_data
import constant_paths
import json


def get_movie_by_id(movie_id: int) -> Movie:
    dao = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.searchByMovieID(movie_id)[0]


# Retuns the movies matching the title as a JSON string
# An example of the JSON string is given below
def get_movie_by_title(title: str) -> str:
    dao = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    movies = dao.searchByTitle(title)
    result_dict = {"movies": []}
    for movie in movies:
        movie_temp = {}
        movie_id = movie.getMovieID()
        movie_temp["movie_id"] = movie_id
        movie_temp["imdb_id"] = get_link_data.get_imdb_id_by_movie(movie_id)
        movie_temp["tmdb_id"] = get_link_data.get_tmdb_id_by_movie(movie_id)
        movie_temp["title"] = movie.getTitle()
        movie_temp["genres"] = movie.getGenres().replace('|', ', ')
        result_dict["movies"].append(movie_temp.copy())

    movie_count = len(movies)
    result_dict["movieCount"] = movie_count
    if movie_count != 0:
        result_dict["hasMovies"] = True
    else:
        result_dict["hasMovies"] = False

    return json.dumps(result_dict, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print(get_movie_by_title("home"))
