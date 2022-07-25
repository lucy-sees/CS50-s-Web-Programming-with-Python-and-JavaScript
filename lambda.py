people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Lucy", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"},
]#nested data structure (dict inside a list)

def f(person):
    return person["house"]
people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)