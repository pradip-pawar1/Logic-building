import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(SCRIPT_DIR, "dummy.json")


def sort_data_map(rtype:str, key: int | str = None, value:str | int = None) -> int | str | None:
        """This method returns the key or value from the vehicles list based on rtype."""
  
        vehicles = {
            0 : "Stop",
            1 : "Car",
            2 : "Bike",
            3 : "Auto",
            4 : "Truck"
        }

        if rtype == "value":
            return vehicles.get(key)
        elif rtype == "key":
            search_val = str(value).title()
            return next((k for k, val in vehicles.items() if val == search_val), None)
        return None

print(sort_data_map(rtype="value", key=2))