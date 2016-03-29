import lesson #Only put this here just so I can't miss out files if needed#
import loaders
import register
import users

"For lecturer to get result, provide feedback"

"For student to get feedback from lecturer"

class Result:
    """  Result Class """
    def __init__(self, ID, username, result, feedback):
        self.testID = ID
        self.username = username
        self.result = result
        self.lecturerfeedback = feedback

    def getresult(self, testID, studentnumber):
        return self.studentnumber
        #return int#

    def providefeedback(self, feedback):
        pass
        #return void#

    def getlecturerfeedback(self, testID, studentnumber):
        #return string#