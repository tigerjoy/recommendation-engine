from dao.movieCycleDAO import MovieCycleDAO
from core.movieCycle import MovieCycle
from get_data import get_movie_cycle_data as gmcd
from update_data import update_movie_cycle_data as umcd
import constant_paths


def add_movie_cycle_data(user_id: int, last_movie_id: int, second_last_movie_id: int, priority: int) -> bool:
    # If no record exists for the user
    if gmcd.get_movie_cycle_data(user_id, priority) is None:
        dao = MovieCycleDAO(constant_paths.CONFIG_FILE_PATH)
        the_record = MovieCycle(user_id, last_movie_id, second_last_movie_id, priority)
        return dao.addRecord(the_record)
    else:
        return umcd.update_movie_cycle_data(user_id, last_movie_id, second_last_movie_id, priority)