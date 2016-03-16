"""
    This file consits of classes that are responsible of loading details
    of accounts from csv files.

    Supported Functionality:
        +Add Account
        +Remove Accounts

    @Maciej_Caputa
"""
import yaml

import users
from lesson import Lesson, Content, Paragraph
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

    def lookUpUsername(self, username):
        """Looks up an username and returns his/her object. If user is not found return None"""
        for i in self.array:
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
        if self.lookUpUsername(username) == None: # Duplicates in one file are *not* permited
            self.array.append(users.Student(username, forename, surname, hashedPassword, year, course))

            with open('database/students.csv', 'a') as csvfile: # a stands for append
                wrtr = csv.writer(csvfile, delimiter=',',)
                wrtr.writerow([username, forename, surname, hashedPassword, year, course])
        else:
            print("Username " + username + " already exits!")


    def removeAccount(self, username):
        """
        This function removes user with given username.
        """
        self.array.remove(self.lookUpUsername(username))

        with open('database/students.csv', 'w') as csvfile:
            for i in self.array:
                wrtr = csv.writer(csvfile, delimiter=',',)
                wrtr.writerow("\n", [i.getUsername(), i.getForename(), i.getSurname(), i.getYear(), i.getCourse()])

class LessonLoader:
    """
    Class to load Lesson objects
    """
    def __init__(self, filenames):
        """
        Load each lesson in the list of filenames provided
        """
        self.array = []

        for filename in filenames:
            with open(filename) as f:
                # data is a dictionary containing the lesson data
                data = yaml.load(f)

                # Create the Paragraph objects
                paragraphs = []
                for i in data["content"]["paragraphs"]:
                    # Image and link are optional so set to None if not present
                    image = i["image"] if "image" in i else None
                    link = i["link"] if "link" in i else None

                    p = Paragraph(i["body"], image, link)
                    paragraphs.append(p)

                # Create the Content object
                content = Content(data["content"]["title"],
                                  data["content"]["introduction"],
                                  paragraphs,
                                  data["content"]["summary"])
                # Create the actual Lesson
                self.array.append(Lesson(data["id"], data["topic"],
                                         data["module"], content))

    def get_lesson(id):
        """
        Return the lesson object with the specified ID, or None if no such
        lesson is found
        """
        for i in self.array:
            if i.lesson_ID == id:
                return i

        return None

    def display(self):
        print()
        for i in self.array:
            print(i)

        print()


database = {}
database["administrators"] = AdministratorLoader("database/administrators.csv")
database["lecturers"] = LecturerLoader("database/lecturers.csv")
database["students"] = StudentLoader("database/students.csv")

database["students"].addAccount("webMattson2", "Natan", "Caputa", "qwerty", 1, "BSc hons Computing and Mathematics")

# This is just for tesing purposes
database["administrators"].display()
database["lecturers"].display()
database["students"].display()

database["lessons"] = LessonLoader(["database/lessons/prob.yaml"])
database["lessons"].display()





