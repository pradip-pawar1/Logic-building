import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(SCRIPT_DIR, "data.json")

with open(file_path, "r") as file:
    data = json.load(file)

# print(f"Path of Test.py : {SCRIPT_DIR}")
# print(f"Path of data.json : {file_path}")
# print(f"Data type : {type(data)}")

key = False

if key:
    print("yes")
else:
    print("no")