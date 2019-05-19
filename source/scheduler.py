from kick import *

class Scheduler:
	def __init__(self, name):
		self.name = name
		self.task = {}

	def add_task(self, kicker, name = None):
		if name == None:
			name = kicker
		self.task.update({name: kicker})
	
	def run(self):
		for n,t in self.task.items():
			#print("eseguo {}".format(n))
			t.kick()