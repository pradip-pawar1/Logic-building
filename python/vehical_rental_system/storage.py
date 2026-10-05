import os
import json

class Data:
    """This classs handels data tasks like reading or writing"""
    # --------------------| Load data and return copy |--------------------
    @staticmethod
    def load_data() -> dict | None:
        """Load data and returns a copy of it form of `dict`"""

        try:
            SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(SCRIPT_DIR, "data.json")
            # Read file 
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        
        except Exception as e:
            print(f"Error occured during data loading: \n{e}")
            return None

    # --------------------| Write data |--------------------
    @staticmethod
    def update_data(data:dict) -> None:
        """Takes new data and update it to main *data* source"""

        try:
            SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(SCRIPT_DIR, "data.json")
            # write file
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)

            print("Data update successfully")

        except Exception as e:
            print(f"Error occured during data updating: \n{e}")