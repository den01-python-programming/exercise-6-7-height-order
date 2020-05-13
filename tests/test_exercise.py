import pytest
import os

def test_exercise():
    os.chdir('src')

    from person import Person
    from room import Room

    room = Room()

    assert room.is_empty()

    room.add(Person("Liam", 182))
    room.add(Person("Ada", 186))

    assert not room.is_empty()
    assert room.shortest() == "Liam"

    room.take()

    assert room.shortest() == "Ada"

    room.take()

    assert room.is_empty()
