import json
import os

from requests.utils import set_environ


class PeopleDict:
    def __init__(self, filename="people.json"):
        self.filename = filename
        self._data = {} #Cache
        self._load_from_file()
        print(self._data) #to check if data contains info from file

    #add or update person's data
    def add_person(self, username, info: dict):
        self._data[username] = info
        self._save_to_file()

    def __setitem__(self, username, info: dict):
        self.add_person(username, info)

    #get data for single person
    def _get_person(self, username):
        return self._data.get(username)

    def __getitem__(self, username):
        return self._get_person(username)

#allows us to iterate
    def __iter__(self):
        return iter(self._data)

    #returns user name and data
    def items(self):
        return self._data.items()

    def _load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf=8") as file:
                    self._data = json.load(file)
            except json.JSONDecodeError:
                print("Wrong json file.")
                self._data = {}

    def _save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self._data, file, ensure_ascii=False, indent=4)