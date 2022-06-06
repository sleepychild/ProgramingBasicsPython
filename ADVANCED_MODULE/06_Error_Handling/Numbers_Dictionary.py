from typing import Dict

numbers_dictionary: Dict = dict()

line: str = input()

while line != "Search":
    number_as_string: str = line
    number: int = int(input())
    numbers_dictionary[number_as_string] = number

line: str = input()

while line != "Remove":
    searched: str = line
    print(numbers_dictionary[searched])

line: str = input()

while line != "End":
    searched: str = line
    del numbers_dictionary[searched]

print(numbers_dictionary)
