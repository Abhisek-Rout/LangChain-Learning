from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name': 'Ravi',
    'age': 36
}

# Here typed dict assist u with data type of the fileds, but it won't do any validation even if u proviide age in string
print(new_person)