
class User:
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg
		

class Administrator(User):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Administrator, self).__init__()
		self.arg = arg
		
class Lecturer(User):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Lecturer, self).__init__()
		self.arg = arg


class Student(User):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Student, self).__init__()
		self.arg = arg
		
		