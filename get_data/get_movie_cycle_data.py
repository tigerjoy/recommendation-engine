from dao.movieCycleDAO import MovieCycleDAO
from core.movieCycle import MovieCycle
import constant_paths


def get_movie_cycle_data(user_id: int) -> MovieCycle:
    dao = MovieCycleDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.getRecordByUser(user_id)

