#!/bin/python3

import os

def gradingStudents(grades):
    for grade in grades:
        print(grade + abs(5 - int(str(grade)[1])))
        if int(str(grade)[1]) < 5:
            rounded = grade + 5 - int(str(grade)[1])

        elif int(str(grade)[1]) > 5:
            rounded = grade + 10 - int(str(grade)[1])
            # if grade(1) > 2 and grade(1) < 5 or grade(1) > 7 and grade(1) < 10:
        if rounded - grade < 3:
            grade = rounded
    return grades


if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
