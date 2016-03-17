"""
    This file consits of classes that are responsible of loading details
    of accounts from csv files.

    Supported Functionality:
        +Add Account
        +Remove Accounts

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

    def searchUsername(self, username):
        """Looks up an username and returns his/her object. If user is not found return None"""
        for i in self.array:
            print(username)
            print(i.getUsername())
            if i.getUsername() == username: # Assumption: username is unique!
                return i

        return None


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


    def addAccount(self, username, forename, surname, hashedPassword, year, course):
        if self.searchUsername(username) == None: # Duplicates in one file are *not* permited
            self.array.append(users.Student(username, forename, surname, hashedPassword, year, course))

            with open('database/students.csv', 'a') as csvfile: # a stands for append   
                wrtr = csv.writer(csvfile, delimiter=',',)
                wrtr.writerow([username, forename, surname, hashedPassword, year, course])
            return True
        else:
            return False


    def removeAccount(self, username):
        """
        This function removes user with given username.
        """
        self.array.remove(self.lookUpUsername(username))

        with open('database/students.csv', 'w') as csvfile:
            for i in self.array:     
                wrtr = csv.writer(csvfile, delimiter=',',)
                wrtr.writerow("\n", [i.getUsername(), i.getForename(), i.getSurname(), i.getYear(), i.getCourse()])


    def logIn(self, username, password):
        for user in self.array:
            print(user.getPassword())
            print(username == user.getUsername())
            print(password == user.getPassword())
            if username == user.getUsername() and password == user.getPassword():
                print(username, password)
                return True

        return False


database = {}
database["administrators"] = AdministratorLoader("database/administrators.csv")
database["lecturers"] = LecturerLoader("database/lecturers.csv")
database["students"] = StudentLoader("database/students.csv")

#database["students"].addAccount("webMattson2", "Natan", "Caputa", "qwerty", 1, "BSc hons Computing and Mathematics")

# This is just for tesing purposes
#database["administrators"].display()
#database["lecturers"].display()
#database["students"].display()








