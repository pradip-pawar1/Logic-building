import os
import json
from main import check_pass


class Admin:
    """Manage all operations including data handeling"""
    def __init__(self, passward:str) -> None:
        self.password = passward

    # --------------------| Load data and return copy |--------------------
    def load_data(self) -> dict:
        """Load data and returns a copy of it form of `dict`"""

        key = check_pass(self.passward) # verify admin

        if key:
            try:
                SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(SCRIPT_DIR, "data.json")
                
                with open(file_path, "r") as file:
                    data = json.load(file)
                return data
            except Exception as e:
                print(f"Error occured during data loading: \n{e}")

        else:
            print("Incorrect password, operation failed!")

    # --------------------| Write data |--------------------
    def update_data(self, data:dict) -> None:
        """Takes new data and update it to main *data* source"""

        key = check_pass(self.password)

        if key:
            try:
                SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(SCRIPT_DIR, "data.json")

                with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)

                print("Succesfully updated data")
            except Exception as e:
                print(f"Error occured during data updating: \n{e}")

        else:
            print("Incorrect password, operation failed!")
            




owner = Admin()

data = owner.load_data("admin01")
data = owner.update_data(data)
# print(data)