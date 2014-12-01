class Invalid_Position_List(Exception):
	'''This exception would be raised if the list of positions is invalid.
	''' 
	def __str__(self):
		return 'Your list of positions is an invalid format.\n' + \
		'Position list should start with [, followed by positive integers which can divide 1000 and end with ]\n' + \
		'\nPlease try again.\n'


class Invalid_Num_Trials(Exception):
	'''This exception would be raised if the input number is invalid.
	''' 
	def __str__(self):
		return 'Your number of trials is an invalid form.\n' + \
		'Number of trials should be a positive integer'
		'\nPlease try again or type \'quit\' to exit.\n'



class Save_Error(Exception):
	'''This exception would be raised if failed to save a file.
	''' 
	pass


class Open_Error(Exception):
	'''This exception would be raised if failed to open a file.
	''' 
	pass