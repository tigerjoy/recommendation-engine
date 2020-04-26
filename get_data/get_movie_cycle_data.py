from dao.movieCycleDAO import MovieCycleDAO
from core.movieCycle import MovieCycle
from typing import List
import constant_paths


def get_movie_cycle_data(user_id: int, priority: int) -> List[MovieCycle]:
    dao = MovieCycleDAO(constant_paths.CONFIG_FILE_PATH)
    return dao.getRecordByUserPriority(user_id, priority)

