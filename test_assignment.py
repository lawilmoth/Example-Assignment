import pytest
from assignment import print_hello, print_hello_person_name, print_hello_person_name_age

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

@pytest.mark.parametrize("name", ["Alice", "Bob", ""])
def test_print_hello_person_name(capsys, name):
    print_hello_person_name(name)
    expected = f"Hello, {name}!"
    captured = capsys.readouterr()
    assert captured.out.strip() == expected

@pytest.mark.parametrize(
    "name,age,expected",
    [
        ("Alice", 30, "Hello, Alice! You are 30 years old. On your birthday, you will be 31."),
        ("Bob", 0, "Hello, Bob! You are 0 years old. On your birthday, you will be 1."),
        ("", 99, "Hello, ! You are 99 years old. On your birthday, you will be 100."),
    ]
)
def test_print_hello_person_name_age(capsys, name, age, expected):
    print_hello_person_name_age(name, age)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected