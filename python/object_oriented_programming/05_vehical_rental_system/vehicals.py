import os
import json

class Vehical:
    def __init__(self, company:str, vhnumber:str, vhtype:str, pwtype:str) -> None:
        self.company = company
        self.vhnumber = vhnumber
        self.vhtype = vhtype
        self.pwtype = pwtype

        

class Car(Vehical):
    def __init__(self, company, vhnumber, vhtype, pwtype, model:str) -> None:
        super().__init__(company, vhnumber, vhtype, pwtype)
        self.model = model

class Bike(Vehical):
    def __init__(self, company, vhnumber, vhtype, pwtype, model:str) -> None:
        super().__init__(company, vhnumber, vhtype, pwtype)
        self.model = model

class Auto(Vehical):
    def __init__(self, company, vhnumber, vhtype, pwtype, model:str):
        super().__init__(company, vhnumber, vhtype, pwtype)
        self.model = model

class Truck(Vehical):
    def __init__(self, company, vhnumber, vhtype, pwtype, model:str, tyers:int) -> None:
        super().__init__(company, vhnumber, vhtype, pwtype)
        self.model = model
        self.tyers = tyers
