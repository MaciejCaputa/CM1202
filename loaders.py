"""
    This file consits of classes that are responsible of loading details
    of accounts from csv files.

    @Maciej_Caputa
"""

import users
import csv


class Loader:
    """docstring for ClassName"""
    def __init__(self):
        self.array = []

    def display(self):
        print()
        for i in self.array:
            print(i)

        print()


class AdministratorLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        super(AdministratorLoader, self).__init__()

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                username, forename, surname, hashedPassword = row
                self.array.append(users.Administrator(username, forename, surname, hashedPassword))


class LecturerLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        super(LecturerLoader, self).__init__()

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                username, forename, surname, hashedPassword, school, modulesTaught = row
                self.array.append(users.Lecturer(username, forename, surname, hashedPassword, school, modulesTaught))


class StudentLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        super(StudentLoader, self).__init__()

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                username, forename, surname, hashedPassword, year, course = row
                self.array.append(users.Student(username, forename, surname, hashedPassword, year, course))


database = {}
database["administrators"] = AdministratorLoader("database/administrators.csv")
database["lecturers"] = LecturerLoader("database/lecturers.csv")
database["students"] = StudentLoader("database/students.csv")

# This is just for tesing purposes
database["administrators"].display()
database["lecturers"].display()
database["students"].display()









