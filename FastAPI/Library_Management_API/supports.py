import json


class Support:
    '''This class provides supporting functions to main API'''
    @classmethod
    def load_data(cls) -> dict:
        '''This method returns the copy of JSON data as a python `dict`'''
        with open("data.json", "r") as file:
            data = json.load(file)

        return data

    @classmethod
    def save_data(cls, data:dict) -> None:
        '''This mathod save the provided data to original JSON data'''
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def get_keys(cls) -> str:
        '''Returns missing or unused keys in between all keys'''
        data = cls.load_data()
        keys = []
        for key in data.keys():
            keys.append(key)

        keys = sorted(keys)

        number = [int(k[1:]) for k in keys]
        min_num = min(number)
        max_num = max(number)

        expected_keys = {f"B{n:03d}" for n in range(min_num, max_num + 1)}
        actual_keys = set(keys)
        missing_keys = sorted(list(expected_keys - actual_keys))

        return missing_keys

    @classmethod
    def create_id(cls) -> str:
        '''returns a key.
        priorities the unused or missing key, if not found then create new key'''
        priority_key = cls.get_keys()

        if not priority_key:
            data = cls.load_data()
            keys = []
            for key in data.keys():
                keys.append(key)
    
            keys = sorted(keys)

            last_num = max([int(k[1:]) for k in keys])
            next_num = last_num + 1
            return f"B{next_num:03d}"
        
        return priority_key[0]