from core.movie import Movie
from dao.movieDAO import MovieDAO
from typing import List
import constant_paths


def get_movie_by_id(movie_id: int) -> Movie:
    dao = MovieDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.searchByMovieID(movie_id)[0]
