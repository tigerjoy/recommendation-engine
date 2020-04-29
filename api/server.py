from flask import Flask, render_template, request, jsonify
from get_data import get_movie_recommendation_data as gmrd
from get_data import get_movie_data as gmd
from get_data import get_average_rating_data as gard
from get_data import get_rating_data as grd
from add_data import add_rating_data as ard

# TODO: Create the flask api in this file and add the necessary imports to call the functions
# This method is called by the run.py file to start the flask server
# TODO: After you've tested your flask app, delete the app.run() and uncomment app.run() in the below function

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/movie.html")
def movie():
    return render_template("movie.html")


# @app.route("/user")
@app.route("/user.html")
def user():
    return render_template("user.html")


@app.route("/search")
def search_movie_by_title():
    title = request.args['title']
    return gmd.get_movie_by_title(title)


@app.route("/get_movies_by_priority")
def get_recommended_movies_by_priority():
    userId = int(request.args['uid'])
    priority = int(request.args['pid'])
    return gmrd.get_recommended_movies(userId, priority)


@app.route("/has_watched")
def has_watched():
    if request.args['uid'] != "null" and request.args['mid'] != "null":
        userId = int(request.args['uid'])
        mid = int(request.args['mid'])
        return grd.has_watched(userId, mid)
    else:
        result_dict = jsonify({
            "user_id": request.args['uid'],
            "movie_id": request.args['mid'],
            "has_watched": False
        })
        return result_dict


@app.route("/get_popular_movies")
def get_popular_movies_for_user():
    userId = int(request.args['uid'])
    return gmrd.get_popular_movies(userId)


@app.route("/get_average_rating")
def get_average_rating_of_movie():
    movieId = int(request.args['mid'])
    return gard.get_average_rating(movieId)


@app.route("/get_rating_by_user")
def get_user_movie_rating():
    if request.args['uid'] != "null" and request.args['mid'] != "null":
        userId = int(request.args['uid'])
        mid = int(request.args['mid'])
        return grd.get_rating_data(userId, mid)
    else:
        result_dict = jsonify({
            "user_id": request.args['uid'],
            "movie_id": request.args['mid'],
            "rating": None
        })
        return result_dict


@app.route("/get_all_users")
def get_list_of_users():
    return grd.get_all_users()


@app.route("/check_user")
def check_user():
    userId = int(request.args['uid'])
    return grd.check_user_exists(userId)


@app.route("/movie_watched")
def is_movie_watched():
    userId = int(request.args['uid'])
    mid = int(request.args['mid'])
    return grd.has_watched(userId, mid)


@app.route("/add_user_rating")
def add_rating():
    # userId = int(request.form['uid'])
    userId = int(request.args['uid'])
    # mid = int(request.form['mid'])
    mid = int(request.args['mid'])
    # rating = float(request.form['rating'])
    rating = float(request.args['rating'])
    status = ard.add_rating(userId, mid, rating)
    resp = {'success': status, "status_code": 200}
    resp = jsonify(resp)
    return resp


def start():
    app.run()


if __name__ == "__main__":
    start()
