from dao.movieCycleDAO import MovieCycleDAO
from core.movieCycle import MovieCycle
import constant_paths


def update_movie_cycle_data(user_id: int, last_movie_id: int, second_last_movie_id: int, priority: int) -> bool:
    the_record = MovieCycle(user_id, last_movie_id, second_last_movie_id, priority)
    dao = MovieCycleDAO(constant_paths.CONFIG_FILE_PATH)

    return dao.updateRecordByUser(the_record)