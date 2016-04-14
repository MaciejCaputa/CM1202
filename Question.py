import csv

class Question():

    '''
    Class to represent a Question
    '''

    _createdQuestions = {} #dictionary of all created questions with ID and Question

    @classmethod
    def _loadQuestions(cls, filename):
        CSV_ID = 0
        CSV_TYPE = 1
        CSV_MODULE = 2
        CSV_TOPIC = 3
        CSV_TEXT = 4
        CSV_CORRECTANSWER = 5
        CSV_MARKS = 6
        CSV_INCORRECTANSWERMARKS = 7
        CSV_OPTIONS = 9

        try:
            with open(filename) as csvfile:
                rdr = csv.reader(csvfile)
                next(rdr, None)

                for row in rdr:
                    if row[CSV_TYPE] == "MC":
                        cls._createdQuestions[row[CSV_ID]] = multipleChoice(row[CSV_ID], row[CSV_MODULE], row[CSV_TOPIC], row[CSV_TEXT], row[CSV_CORRECTANSWER], row[CSV_MARKS], row[CSV_INCORRECTANSWERMARKS], row[CSV_OPTIONS:])
                    else:
                        cls._createdQuestions[row[CSV_ID]] = openQuestion(row[CSV_ID], row[CSV_MODULE], row[CSV_TOPIC], row[CSV_TEXT], row[CSV_CORRECTANSWER], row[CSV_MARKS], row[CSV_INCORRECTANSWERMARKS])
        except csv.Error:
            return None

    @classmethod
    def getQuestion(cls, question_ID):
        try:
            if len(cls._createdQuestions) == 0:
                cls._loadQuestions("Questions.csv")

            return cls._createdQuestions[question_ID]
        except KeyError:
            return None

    #Instance Methods
    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks, incorrectAnswerMarks):
        self._question_ID = question_ID
        self._module = module
        self._topic = topic
        self._questionText = questionText
        self._correctAnswer = correctAnswer
        self._availableMarks = int(marks)
        self.incorrectAnswerMarks = int(incorrectAnswerMarks)
        self._studentFinalAnswers = {}
        Question._createdQuestions[self._question_ID] = self

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
        try:
            return self._studentFinalAnswers[studentID][0]
        except KeyError:
            return None

    def marksAwarded(self, studentID):
        try:
            if self._studentFinalAnswers[studentID][1] == True:
                return self._availableMarks
            else:
                return self.incorrectAnswerMarks
        except KeyError:
            return None

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

    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks, incorrectAnswerMarks):
        super().__init__(question_ID, module, topic, questionText, correctAnswer, marks, incorrectAnswerMarks)

    def isQuestionMultipleChoice(self): #checks if a question is multiple choice
            return False


class multipleChoice(Question):

    '''
    Class to represent a Multiple Choice Question
    '''

    def __init__(self, question_ID, module, topic, questionText, correctAnswer, marks, incorrectAnswerMarks, options): #constructor
        super().__init__(question_ID, module, topic, questionText, correctAnswer, marks, incorrectAnswerMarks)
        self._options = options

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