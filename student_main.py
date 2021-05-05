from linked_list import LinkedList
from operator import itemgetter


def read_from_txt():
    """
    Function reads the data from "students_read.txt",
    saves the data to the list and returns: the list with data

    "students_read.txt" represented in CSV (Comma Separated Values) format:
    <Name>,<Surname>,<Birth date>,<Marks> - example

    Students with average point less than 4.5 are not added
    """
    students_list = []

    file = open("students_read.txt", "r", encoding="utf-8")
    file.readline()

    for student in file:
        marks = student[:-1].split(',')[3].split(' ')
        marks_average = 0

        for mark in marks:
            marks_average += int(mark)

        if (marks_average / len(marks)) > 4.5:
            students_list.append(student[:-1].split(','))

    students_list.sort(key=lambda x: x[1])
    students_list.reverse()

    return students_list


def add_to_linked(students_list):
    """
    Function adds the data from list to linked list

    returns: linked list with data
    """
    students_linked = LinkedList()

    for student in students_list:
        students_linked.add(student)

    return students_linked


def write_to_txt():
    """
    Function writes the data in "students_write.txt",
    returns: None

    "students_write.txt" represented in CSV (Comma Separated Values) format:
    <Name>,<Surname>,<Birth date>,<Marks> - example
    """
    students_linked = add_to_linked(read_from_txt())

    file = open("students_write.txt", "w", encoding="utf-8")
    file.writelines("name,surname,birthday,marks\n")

    while not students_linked.empty():
        stud = students_linked.delete(students_linked.delete(0).item).item
        file.writelines(stud[0] + ',' + stud[1] + ',' + stud[2] + ',' + stud[3] + '\n')


if __name__ == '__main__':
    write_to_txt()
