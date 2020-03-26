import json

config_path = input("Enter the absolute path of the config file: ")
db_path = input("Enter the absolute path of the db file: ")

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

