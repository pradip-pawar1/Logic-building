from storage import Data

class Vehicle:
    """This class represents one physical unit. It knows its own details and current rental status."""

    # --------------------| Check avalibility of vehicle |--------------------

    def vehicle_status(self, vehicle_inv_no:str, vehicle_type:str) -> str | None:
        """This method check that perticular vehicle is available or rented"""
        data = Data.load_data()

        specific_vehicle = next((item for item in data[vehicle_type] if item["Inv. No."] == vehicle_inv_no), None)

        if not specific_vehicle:
            print("Data unavaliable")
            return None
        elif specific_vehicle["Rental status"] == True:
            return "Unavaliable"
        else:
            return "Avaliable"

    # --------------------| Show all vehicles & check avalibility |--------------------
    
    def show_vehicles(self, vehicle_type:str) -> None:
        """This method show customer or user all the avaliable or unavaliable
        vehicles present on the database, and returns that the selected vehicles status"""

        data = Data.load_data()
        i = 1
        
        for vehicle in data[vehicle_type]:
            name = vehicle["Name"]
            company = vehicle["Company"]
            number = vehicle["Inv. No."]

            print(f"{i} | Vehicle : {name} | Company : {company} | Number : {number}")
            i += 1

        choice = input(f"Want to select any {vehicle_type}? Enter the number: ")

        # check if that vehicle is avaliable or not?
        return self.vehicle_status(choice, vehicle_type)

