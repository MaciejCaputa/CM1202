import csv
from Question import Question
        
class Test():
        
    '''
    Class to represent a Test
    '''
    
    _createdTests = {} #dictionary of all created Tests
    
    @classmethod
    def _loadTests(cls, filename):
        CSV_ID = 0
        CSV_MODULE = 1
        CSV_TOPIC = 2
        CSV_NAME = 3
        CSV_INTRODUCTIONTEXT = 4
        CSV_QUESTIONIDS = 5
        
        try:
            with open(filename) as csvfile:
                rdr = csv.reader(csvfile)
                next(rdr, None)
                
                for row in rdr:
                    testQuestions = []
                    
                    for q in row[CSV_QUESTIONIDS:]:
                        testQuestions.append(Question.getQuestion(q))
                                      
                    cls._createdTests[row[CSV_ID]] = Test(row[CSV_ID], row[CSV_MODULE], row[CSV_TOPIC], row[CSV_NAME], row[CSV_INTRODUCTIONTEXT], testQuestions)
        except csv.Error: ###WHICH EXCEPION TO RAISE???
            return None
    
    @classmethod
    def getTest(cls, test_ID):
        try:
            if len(cls._createdTests) == 0:
                cls._loadTests("Test.csv")
                
            return cls._createdTests[test_ID]
        except KeyError:
            return None
    
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
        try:
            return self._studentFinalAnswers[studentID]
        except KeyError:
            return None
    
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