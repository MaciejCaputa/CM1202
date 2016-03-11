"""
	This file consits of classes that are responsible of loading details
	of accounts from csv files.
	
    @Maciej Caputa
"""

import users
import csv

class Loader:
    """docstring for ClassName"""
    def __init__(self):
        self.array = []

    def display(self):
        for i in self.administrators:
                print(i)


class AdministratorLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        super(AdministratorLoader, self).__init__()

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                print(row)
                username, forename, surname, hashedPassword = row
                self.array.append(users.Administrator(username, forename, surname, hashedPassword))




class LecturerLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        self.administrators = []

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                
                print(row)
                username, forename, surname, hashedPassword = row
                self.administrators.append(Administrator(username, forename, surname, hashedPassword))


class StudentLoader(Loader):
    """docstring for Loader"""
    def __init__(self, fileName):
        self.administrators = []

        with open(fileName) as csvfile:
            rdr = csv.reader(csvfile)

            for row in rdr:
                print(row)
                username, forename, surname, hashedPassword = row
                self.administrators.append(Administrator(username, forename, surname, hashedPassword))


admins = AdministratorLoader("database/administrators.csv")