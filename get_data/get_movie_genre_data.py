from core.movieGenre import MovieGenre
from dao.movieGenreDAO import MovieGenreDAO
from typing import List
import constant_paths


# Returns a list of genre ids of a movie
def get_movie_genre_ids(movie_id: int) -> List[int]:
    dao = MovieGenreDAO(constant_paths.CONFIG_FILE_PATH)
    output = dao.searchByMovieID(movie_id)
    if len(output) == 0:
        return []
    else:
        genre_list = []
        for movie_genre in output:
            genre_list.append(movie_genre.getGenreID())
        return genre_list
