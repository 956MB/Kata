#!/usr/bin/python3

# Who has the most money?
# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

def most_money(students):
    if len(students) == 1:
        return students[0].name

    dollars = []

    for i in students:
        _5 = i.fives * 5
        _10 = i.tens * 10
        _20 = i.twenties * 20
        dollars.append(_5 + _10 + _20)

    if len(set(dollars)) <= 1:
        return 'all'

    return students[dollars.index(max(dollars))].name

if __name__ == '__main__':
    cam = Student("Cameron", 2, 2, 0)
    geoff = Student("Geoff", 0, 3, 0)
    phil = Student("Phil", 2, 2, 1)

    print(most_money([cam, geoff, phil]), "Phil")
    print(most_money([cam, geoff]), "all")
    print(most_money([geoff]), "Geoff")
