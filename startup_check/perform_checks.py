from get_data import get_temp_recommendation as gtr
from get_data import get_generating_recommendation_data as ggrd
from generate_data import generateRecommendations as gr
from delete_data import delete_temp_recommedation_data as dtrd
from datetime import datetime
import constant_paths
import threading


# Writes to log file
def writeLog(output, filename):
    with open(filename, "a") as file:
        timestamp = datetime.strftime(datetime.now(), "[ %m-%d-%Y %H:%M:%S ] : ")
        print(timestamp + str(output), file=file)


def start_generation(user_id: int):
    x = threading.Thread(target=gr.largestIntersectionSQL, args=(user_id, True))
    x.start()


# Method to perform startup checks
def start_checks():
    timestamp = datetime.strftime(datetime.now(), "%m-%d-%Y %H-%M-%S")
    log_file_name = constant_paths.LOG_FILE_PATH + "\\startup_check_log_at_" + timestamp + ".txt"
    print("Start up check started...")
    writeLog("Start up check started...", log_file_name)
    user_ids = gtr.get_all_user_id()
    for user_id in user_ids:
        writeLog(f"Checking for User {user_id} in temp recommendation", log_file_name)
        if ggrd.check_user_exists(user_id):
            writeLog(f"Recommendation generation pending for User {user_id}", log_file_name)
            writeLog(f"Starting generation process...", log_file_name)
            start_generation(user_id)
        else:
            writeLog(f"Recommendation generation complete for User {user_id}"), log_file_name
            writeLog("Deleting old temporary recommendations", log_file_name)
            dtrd.delete_temp_recommendation(user_id)
    print("Start up check finished!")
    writeLog("Start up check finished!", log_file_name)