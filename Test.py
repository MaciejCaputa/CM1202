import csv
from Question import Question
        
        
class Test():
    _createdTests = {} #dictionary of all created Tests
        
    '''
    Class to represent a Test
    '''
    
    @classmethod
    def _loadTests(cls, filename):
        with open(filename) as csvfile:
            rdr = csv.reader(csvfile)
            next(rdr, None)
            
            for row in rdr:
                testQuestions = []
                
                for q in row[5:]:
                    testQuestions.append(Question.getQuestion(q))
                                  
                cls._createdTests[row[0]] = Test(row[0], row[1], row[2], row[3], row[4], testQuestions)
    
    @classmethod
    def getTest(cls, test_ID):
        if len(cls._createdTests) == 0:
            cls._loadTests("Test.csv")
            
        return cls._createdTests[test_ID]
    
    #Instance Methods
    def __init__(self, test_ID, module, topic, testName, introductionText, questions):
        self._test_ID = test_ID
        self._module = module
        self._topic = topic
        self._testName = testName
        self._introductionText = introductionText
        self._testQuestions = questions
        self._studentFinalAnswers = {}
        Test._createdTests[self._test_ID] = self

    def getTestID(self):
        return self._test_ID
    
    def getModule(self):
        return self._module
    
    def getTopic(self):
        return self._topic
    
    def getTestName(self):
        return self._testName
    
    def getIntroductionText(self):
        return self._introductionText
    
    def addQuestionResult(self, studentID, question):
        try:
            self._studentFinalAnswers[studentID] += question.marksAwarded(studentID)
        except KeyError:
            self._studentFinalAnswers[studentID] = question.marksAwarded(studentID)
    
    def getTestResult(self, studentID):
        return self._studentFinalAnswers[studentID]
    
    def getNextQuestion(self):
        for q in self._testQuestions:
            yield q
    
def testMain(): #FOR TESTING PURPOSES ONLY
    test1 = Test.getTest("1")
    studentID = "01"

    print("Test 1")
    print("ID = " + test1.getTestID())
    print("Module = " + test1.getModule())
    print("Topic = " + test1.getTopic())
    print("Test Name = " + test1.getTestName())
    print("Introduction Text = " + test1.getIntroductionText())
    
    for q in test1.getNextQuestion():
        print("\nQuestion " + q.getQuestionID())
        print(q.getQuestionText())
        print("Marks available = " + str(q.getAvailableMarks()))
        
        if(q.isQuestionMultipleChoice()):
            print("Options: ")
            
            for o in q.getOptions(): 
                print((q.getOptions().index(o) + 1), o)
        
        print("Submitting answer 1")
        print("Is Answer Correct? = " + str(q.isAnswerCorrect(studentID, "1")))
        print("Correct Answer = " + q.getCorrectAnswer())
        print("Submitted Answer = " + q.getSubmittedAnswer(studentID, ))
        print("Marks Awarded = " + str(q.marksAwarded(studentID)))
        test1.addQuestionResult(studentID, q)
    print("\nTest Result = " + str(test1.getTestResult(studentID)))
    
if __name__ == "__main__":
    testMain()