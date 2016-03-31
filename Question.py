import csv

INCORRECTANSWERMARKS = 0
        
        
class Question():
    _createdQuestions = {} #dictionary of all created questions with ID and Question
        
    '''
    Class to represent a Question
    '''
    
    @classmethod
    def _loadQuestions(cls, filename):
        with open(filename) as csvfile:
            rdr = csv.reader(csvfile)
            next(rdr, None)
            
            for row in rdr:
                if row[1] == "MC":
                    cls._createdQuestions[row[0]] = multipleChoice(row[0], row[2], row[3], row[4], row[5], row[6], row[8:])
                else:  
                    cls._createdQuestions[row[0]] = openQuestion(row[0], row[2], row[3], row[4], row[5], row[6])
                     
    @classmethod
    def getQuestion(cls, question_ID):
        if len(cls._createdQuestions) == 0:
            cls._loadQuestions("Questions.csv")
            
        return cls._createdQuestions[question_ID]
    
    #Instance Methods
    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks):
        self._question_ID = question_ID
        self._module = module
        self._topic = topic
        self._questionText = questionText
        self._correctAnswer = correctAnswer
        self._availableMarks = int(marks)
        self._studentFinalAnswers = {}
        Question._createdQuestions[self._question_ID] = self
    
    def _createQuestionText(self, filename, textTemplateNumber): #creates the question text using templates from a file
        pass
    
        '''
        - import template file
        - decide which template to use
        - generate random number(s)
        - fill in template space(s) with generated number(s)
        - return _questionText
        '''

    def getQuestionID(self):
        return self._question_ID
    
    def getModule(self):
        return self._module
    
    def getTopic(self):
        return self._topic
    
    def getQuestionText(self):
        return self._questionText
    
    def getCorrectAnswer(self):
        return self._correctAnswer
    
    def getAvailableMarks(self):
        return self._availableMarks
    
    def getSubmittedAnswer(self, studentID):
        return self._studentFinalAnswers[studentID][0]
    
    def marksAwarded(self, studentID):
        if self._studentFinalAnswers[studentID][1] == True: 
            return self._availableMarks
        else:
            return INCORRECTANSWERMARKS
    
    def isAnswerCorrect(self, studentID, studentAnswer):
        if self._correctAnswer == studentAnswer: 
            self._studentFinalAnswers[studentID] = (studentAnswer, True)
            return True
        else:
            self._studentFinalAnswers[studentID] = (studentAnswer, False)
            return False
    
    
class openQuestion(Question):
    
    '''
    Class to represent an Open Question
    '''
    
    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks):
        super().__init__(question_ID, module, topic, questionText, correctAnswer, marks)
    
    def createQuestionAnswer(self, filename, answerTemplateNumber):
        with open(self.filenme) as csvfile:
            rdr = csv.reader(csvfile)
            
            for row in rdr:
                pass
            
    def isQuestionMultipleChoice(self): #checks if a question is multiple choice
            return False
        
    
class multipleChoice(Question):
    
    '''
    Class to represent a Multiple Choice Question
    '''
    
    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks, options): #constructor
        super().__init__(question_ID, module, topic, questionText, correctAnswer, marks)
        self._options = options
    
    def createQuestionAnswers(self, filename, answerTemplateNumber, numberOfAnswers): #returns a list of answers
        with open(self.filenme) as csvfile:
            rdr = csv.reader(csvfile)
            
            for row in rdr:
                pass
         
    def getOptions(self): 
        return self._options

    def isQuestionMultipleChoice(self): #checks if a question is multiple choice
        return True
                
def main(): #FOR TESTING PURPOSES ONLY

    question1 = Question.getQuestion("1")
    question2 = Question.getQuestion("2")

    print("Question 1")
    if(question1.isQuestionMultipleChoice()):
        print("Multiple Choice Questions")
        print("Options: ")
        print(question1.getOptions())
        
    print("Is Answer Correct?")
    print(question1.isAnswerCorrect("01", "1"))

    print("Question 2")
    
    if(question2.isQuestionMultipleChoice()):
        print("Multiple Choice Questions")
        print("Options: ")
        print(question2.getOptions())
        
    print("Is Answer Correct?")   
    print(question2.isAnswerCorrect("01", "1/2"))
    
    
if __name__ == "__main__":
    main()