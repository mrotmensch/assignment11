#Invalid integer
class IntegerErr(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#Invalid shares
class PositionErr(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message
	
