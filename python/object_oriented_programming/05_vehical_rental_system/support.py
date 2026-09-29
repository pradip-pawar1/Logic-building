class Supports:
    """This class is for supporting other main funcinality in ocre operations"""

    @staticmethod
    def check_pass(password:str) -> bool:
        """This methods checks that the person wants to perform operation is it a valid person or not."""
        if password == "admin01":
            return True
        return False

    @staticmethod
    def take_vehicale() -> int:
        """This method ask user to select which details he wants to see and return choice in `int`"""

        vehicles = {
            0 : "Stop",
            1 : "Cars",
            2 : "Bike",
            3 : "Auto",
            4 : "Truck"
        }
        
        for key, val in vehicles.items():
            print(f"{key} : {val}")

        try:
            choice = int(input("Enter the vehical to see details : "))
        except ValueError:
            print(f"Please provide valid input. {ValueError}")

        return choice

    @staticmethod
    def sort_data_map(rtype:str, key: int | str = None, value:str | int = None) -> int | str | None:
        """This method returns the key or value from the vehicles list based on rtype."""
  
        vehicles = {
            1 : "cars",
            2 : "bike",
            3 : "auto",
            4 : "truck"
        }

        if rtype == "value":
            return vehicles.get(key)
        elif rtype == "key":
            search_val = str(value).lower()
            return next((k for k, val in vehicles.items() if val == search_val), None)
        return None