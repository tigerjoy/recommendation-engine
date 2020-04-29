import createConfig
from api import server
from startup_check import perform_checks
from get_data import get_movie_recommendation_data as gmrd
from get_data import get_movie_data as gmd
from get_data import get_average_rating_data as gard
from get_data import get_rating_data as grd
from add_data import add_rating_data as ard

# Write all your test code here and delete afterwards
if __name__ == "__main__":
    # Do not remove the below lines
    perform_checks.start_checks()

    # print("\nGet recommended movies for User 189 and Priority 1")
    # print(gmrd.get_recommended_movies(189, 1))
    # print("\nGet Popular Movies for User 189")
    # print(gmrd.get_popular_movies(189))
    # print("\nSearch movie by title")
    # print(gmd.get_movie_by_title("mission"))
    # print("\nGet Average Rating of Movie with id 648")
    # print(gard.get_average_rating(648))
    # print("\nGet the Rating given by User 189 for movie with id 648")
    # print(grd.get_rating_data(189, 648))
    # print("\nGet a list of all user ids")
    # print(grd.get_all_users())

    # To add data to ratings table
    # DO NOT RUN UNLESS NEEDED
    # ard.add_rating(189, 648, 4.5)
    server.start()
