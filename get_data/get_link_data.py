from dao.linkDAO import LinkDAO
import constant_paths


# Returns the IMDB id by movie, if the movie_id
# does not exist "" is returned
def get_imdb_id_by_movie(movie_id: int) -> str:
    dao = LinkDAO(constant_paths.CONFIG_FILE_PATH)
    result = dao.searchByMovieID(movie_id)
    if len(result) != 0:
        return "tt{:07}".format(result[0].getIMDBID())
    else:
        return ""


# Returns the TBDB id by movie, if the movie_id
# does not exist "" is returned
def get_tmdb_id_by_movie(movie_id: int) -> str:
    dao = LinkDAO(constant_paths.CONFIG_FILE_PATH)
    result = dao.searchByMovieID(movie_id)
    if len(result) != 0:
        return str(result[0].getTMDBID())
    else:
        return ""


if __name__ == "__main__":
    print(get_imdb_id_by_movie(260))