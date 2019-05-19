from observer import *


class GPS_Quality(Subscriber):
	def __init__(self): 
		self.validity ='V'
		self.pos = 2
		Subscriber.__init__(self, "Latitude")
		pass

	def set(self, sentence):
		split =sentence.split(',') 
		self.validity = split[self.pos]

	def get(self):
		#print("da get: {}".format(self.validity))

		return self.validity

	def toString(self):
		return "Quality()"
