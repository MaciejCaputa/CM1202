from lesson import * #Only put this here just so I can't miss out files if needed#
from loaders import *
from register import *
from users import *
from Test import *
from LogIn import *
from register import *
from HomePage import *
from TestGUI import *

"Storing the result for lecturer to access later"

class Result:
    """  Result Class """
    def __init__(self, ID, username, result, lecturerfeedback):
        self.testID = ID
        self.username = username
        self.result = result
        self.lecturerfeedback = lecturerfeedback

    def getResult(self, studentID):
        return getTestResult(studentID)
        #return int#

    def storeResult(self, studentID, test):
        with open('C:/Users/DomLaptop/Documents/LessonCourse/CM1202/StoreResults.csv', 'a') as f:  
            w = csv.DictWriter(f, ["studentID", "TestID", "Total"])
            testing = {}
            testing = {"studentID":studentID, "TestID":test.getTestID(), "Total": test.getTestResult(studentID)}
            w.writerow(testing)
        #return void#

    def provideFeedback(self, lecturerfeedback):
        return lecturerfeedback
        #return void#

    def getlecturerfeedback(self, lecturerfeedback):
        return lecturerfeedback
        #return string#
