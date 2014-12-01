class inValidInputException(Exception): 
	"""Raise when the user inputs an invalid format in either position or num_trials in function investment_simulation. """
	pass

class inValidInputFormat(Exception):
	"""Raise when the user inputs an invalid format in raw_input. """
	pass
	
class writeInTextException(Exception):
	"""Raise when program cannot write into a given text file. """
	pass

class saveInPdfException(Exception):
	"""Raise when program cannot save figures into pdf. """
	pass