"""
	@Maciej Caputa
"""

class User:
	"""docstring for ClassName"""
	def __init__(self, username, forename, surname, hashedPassword):
		self.__username = username
		self.__forename = forename
		self.__surname = surname
		self.__hashedPassword = hashedPassword

	def getUsername(self):
		return self.__username

	def getForename(self):
		return self.__forename

	def getSurname(self):
		return self.__surname



class Administrator(User):
	"""docstring for ClassName"""
	pass
		

class Lecturer(User):
	"""docstring for ClassName"""
	def __init__(self, username, forename, surname, hashedPassword, school, modulesTaught):
		super(Lecturer, self).__init__(username, forename, surname, hashedPassword)
		self.__school = school
		self.__modulesTaught = modulesTaught


class Student(User):
	"""docstring for ClassName"""
	def __init__(self, username, forename, surname, hashedPassword, year, course):
		super(Student, self).__init__(username, forename, surname, hashedPassword)
		self.__year = year
		self.__course = course
		
	def getYear(self):
		return self.__year

	def getCourse(self):
		return self.__course

