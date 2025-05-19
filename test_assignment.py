import pytest

from assignment import return_hello, return_hello_person_name, return_hello_person_name_age
def test_return_hello():
    assert return_hello() == "Hello, World!"

def test_return_hello_person_name():
    assert return_hello_person_name("Alice") == "Hello, Alice!"
    assert return_hello_person_name("Bob") == "Hello, Bob!"
    assert return_hello_person_name("Charlie") == "Hello, Charlie!"

def test_return_hello_person_name_age():
    assert return_hello_person_name_age("Alice", 30) == "Hello, Alice! You are 30 years old. On your birthday, you will be 31."
    assert return_hello_person_name_age("Bob", 25) == "Hello, Bob! You are 25 years old. On your birthday, you will be 26."
    assert return_hello_person_name_age("Charlie", 40) == "Hello, Charlie! You are 40 years old. On your birthday, you will be 41."
    assert return_hello_person_name_age("", 0) == "Hello, ! You are 0 years old. On your birthday, you will be 1."


