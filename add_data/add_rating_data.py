from dao.ratingDAO import RatingDAO
from core.rating import Rating
from update_data import update_ratings_data as urd
from add_data import add_average_rating_data as aard
from add_data import add_user_movie_count_data as aumcd
from get_data import get_rating_data as grd
from get_data import get_movie_genre_data as gmgd
import constant_paths


# This method adds a rating entry for a user, movie if it does not exist
# otherwise updates existing record
def add_rating_data(userId: int, movieId: int, rating: float) -> bool:
    dao = RatingDAO(constant_paths.CONFIG_FILE_PATH)
    # If rating data already exists, update the entry in table
    if grd.get_rating_by_user_movie(userId, movieId) is not None:
        return urd.update_rating_data(userId, movieId, rating)
    # If rating does not exist, add it to the table
    else:
        the_rating = Rating(userId, movieId, rating)
        return dao.addRatingByUser(the_rating)


# Interface for Apurba
def add_rating(user_id: int, movie_id: int, rating: float) -> bool:
    # Check if the user has already watched the movie and is giving a new rating
    has_watched = grd.get_rating_by_user_movie(user_id, movie_id) is None

    # Add record to the rating table
    status_1 = add_rating_data(user_id, movie_id, rating)

    # Updated average rating
    new_avg_rating = grd.get_average_rating_by_movie(movie_id)

    # Add the updated average rating to average_rating table
    status_2 = aard.add_average_rating_data(movie_id, new_avg_rating)

    # If the user has already watched the movie
    # no need to increment its watch count
    status_3 = has_watched

    if not has_watched:
        # Get the genre ids for the movie
        genre_ids = gmgd.get_movie_genre_ids(movie_id)

        # Update the watch counts in user_movie_genre_wise_count
        status_3 = aumcd.add_count(user_id, genre_ids)

    return status_1 and status_2 and status_3


if __name__ == "__main__":
    print(add_rating(1, 1, 4.0))
