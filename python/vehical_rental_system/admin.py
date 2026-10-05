import os
import json

from support import Supports
from storage import Data


class Admin:
    """Manage all operations including data handeling"""
    def __init__(self, password:str) -> None:
        self.password = password

    # --------------------| View data |--------------------
    def view_fleet(self) -> None:
        """Show owner all the vehicals and their relative data"""

        key = Supports.check_pass(self.password)

        if key:
            while True:
                user_choice = Supports.take_vehicale()

                if user_choice != 0:
                    vehical_val = Supports.sort_data_map(rtype= "value", key=user_choice)
                    data = Data.load_data() # load data

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
# owner.view_fleet()