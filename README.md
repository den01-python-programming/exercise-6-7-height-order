# Exercise 6.7 Height Order

A `Person` class is included in the exercise template. A person has a name and a height. In this exercise, we'll implement a `Room` class, which can be used to add people and order them according to their height -- taking a person out of the room always returns the shortest person.

The class should eventually work in the following way.

## Room

Create `Room` class. The class should contain a list of persons as an instance variable, and it should have a parameterless constructor. In addition, add the following methods to the class:

- `def add(self, person)` - add the person passed as a parameter to the list.
- `def is_empty()` - returns a `boolean`-type value `True` or `False`, that tells whether the room is empty or not.
- `def get_persons()` - returns a list of the persons in the room.

```python
room = Room()
print("Empty room? " + str(room.is_empty()))
room.add(Person("Lea", 183))
room.add(Person("Kenya", 182))
room.add(Person("Auli", 186))
room.add(Person("Nina", 172))
room.add(Person("Terhi", 185))
print("Empty room? " + str(room.is_empty()))

print()
for person in room.get_persons():
    print(person)
```

```plaintext
Empty room? true
Empty room? false

Lea (183 cm)
Kenya (182 cm)
Auli (186 cm)
Nina (172 cm)
Terhi (185 cm)
```

## Shortest person

Add a `def shortest()` method to the `Room` class, which returns the shortest person added to the room. If the room is empty, a null reference is returned. The method should not remove a person from the room.

```python
room = Room()
print("Shortest: " + str(room.shortest()))
print("Empty room? " + str(room.is_empty()))
room.add(Person("Lea", 183))
room.add(Person("Kenya", 182))
room.add(Person("Auli", 186))
room.add(Person("Nina", 172))
room.add(Person("Terhi", 185))
print("Empty room? " + str(room.is_empty()))

print()
for person in room.get_persons():
    print(person)

print()
print("Shortest: " + str(room.shortest()))
print()
for person in room.get_persons():
    print(person)
```

```plaintext
Shortest: null
Empty room? true
Empty room? false

Lea (183 cm)
Kenya (182 cm)
Auli (186 cm)
Nina (172 cm)
Terhi (185 cm)

Shortest: Nina (172 cm)

Lea (183 cm)
Kenya (182 cm)
Auli (186 cm)
Nina (172 cm)
Terhi (185 cm)
```

## Taking from a room

Add a `def take()` method to the `Room` class, which takes the shortest person in the room. When a room is empty, it returns a `None` reference.

```python
room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 182))
room.add(Person("Auli", 186))
room.add(Person("Nina", 172))
room.add(Person("Terhi", 185))

print()
for person in room.get_persons():
    print(person)

print()
print("Shortest: " + str(room.take()))
print()
for person in room.get_persons():
    print(person)
```

```plaintext
Lea (183 cm)
Kenya (182 cm)
Auli (186 cm)
Nina (172 cm)
Terhi (185 cm)

Shortest: Nina (172 cm)

Lea (183 cm)
Kenya (182 cm)
Auli (186 cm)
Terhi (185 cm)
```

It's now possible to print the persons in height order.

```python
room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 182))
room.add(Person("Auli", 186))
room.add(Person("Nina", 172))
room.add(Person("Terhi", 185))

while (not room.is_empty()):
    print(room.take())
```

```plaintext
Nina (172 cm)
Kenya (182 cm)
Lea (183 cm)
Terhi (185 cm)
Auli (186 cm)
```
