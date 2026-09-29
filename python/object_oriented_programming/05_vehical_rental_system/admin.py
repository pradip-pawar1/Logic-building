import os
import json

from support import Supports


class Admin:
    """Manage all operations including data handeling"""
    def __init__(self, password:str) -> None:
        self.password = password

    # --------------------| Load data and return copy |--------------------
    def load_data(self) -> dict | None:
        """Load data and returns a copy of it form of `dict`"""

        key = Supports.check_pass(self.password) # verify admin

        if key:
            try:
                SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(SCRIPT_DIR, "dummy.json")
                # Read file 
                with open(file_path, "r") as file:
                    data = json.load(file)
                return data
            except Exception as e:
                print(f"Error occured during data loading: \n{e}")

        else:
            print("Incorrect password, operation failed!")
            return None

    # --------------------| Write data |--------------------
    def update_data(self, data:dict) -> None:
        """Takes new data and update it to main *data* source"""

        key = Supports.check_pass(self.password)

        if key:
            try:
                SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(SCRIPT_DIR, "dummy.json")
                # write file
                with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)

                print("Succesfully updated data")
            except Exception as e:
                print(f"Error occured during data updating: \n{e}")

        else:
            print("Incorrect password, operation failed!")

    # --------------------| View data |--------------------
    def view_fleet(self) -> None:
        """Show owner all the vehicals and their relative data"""

        key = Supports.check_pass(self.password)

        if key:
            while True:
                user_choice = Supports.take_vehicale()

                if user_choice != 0:
                    vehical_val = Supports.sort_data_map(rtype= "value", key=user_choice)
                    data = self.load_data() # load data

                    print("\n")
                    for k, v in data[vehical_val].items():
                        print(f"{k} : {v}")
                    print()
                    
                elif user_choice > 4:
                    print("Please choose valid option")

                else:
                    break

            print("Operation successfully completed!")

        else:
            print("Incorrect password, operation failed!")


owner = Admin("admin01")
owner.view_fleet()
# owner.load_data()