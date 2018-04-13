class Dog(object):

	def __init__(self):
		pass

	def __del__(self):
		pass

	def __str__(self):
		print('string method')
		return 'describtion of method'

	def __new__(cls):
		print('new method...')
		object.__new__(cls)