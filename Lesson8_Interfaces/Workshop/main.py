from Lesson8_Interfaces.Workshop.PeopleDict import PeopleDict

if __name__ == "__main__":
    pd = PeopleDict()

#adding person to a dictionary
    # pd.add_person("Jan.Kowalski", {"name": "Jan", "age": 25, "city": "Warsaw"}) <-old version of coding masked with __setitem__
    # print(pd._data)

    pd["Janusz.Kowalski"] = {"name": "Janusz", "age": 50, "city": "Sosnowiec"} #using __setitem__
    print(pd._data)

#Getting persons
    print(pd["Janusz.Kowalski"])

    for username in pd:
        print(f"Username: {username}")

    for username, info in pd.items():
        print(f"Username: {username} -> {info}")