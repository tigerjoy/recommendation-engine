import json
import os

if not os.path.isfile("config/db_properties.json"):
    print("FATAL ERROR: Could not locate db_properties.json file.")
    print("Make sure it is located at config/db_properties.json")
elif not os.path.isfile("db/all.db"):
    print("FATAL ERROR: Could not locate all.db file.")
    print("Make sure it is located at db/all.db")
else:
    config_path = os.path.abspath("config/db_properties.json")
    db_path = os.path.abspath("db/all.db")

    print("Setting up the config file...")

    content = None
    with open(config_path, "r+") as file:
        content = json.loads(file.read())
        for key in content:
            content[key]["dbURL"] = db_path
        # Move to the beginning of the file
        file.seek(0)
        file.write(json.dumps(content, indent=4))
        file.truncate()

    print("Created config file succesfully!")
