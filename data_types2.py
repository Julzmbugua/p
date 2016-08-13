# Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
# Complete the test to produce the perfect function that accounts for all expectations.

# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist

def data_type(data):
	if type(data) == None:
		return 'no value'
	if type(data) == str:
		return len(data)
	elif type(data) == bool:
		return data
	elif type(data) == int:
		if data < 100:
			return "less than 100"
		elif data == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif type(data) == list:
		if len(data) < 3:
			return None
		else:
			return data[2]
# print data_type(True)

import unittest

class Data_type_test(unittest.TestCase):
	def test_data_type(self):
		self.assertEqual(data_type(1), "less than 100")
		self.assertEqual(data_type(100), "equal to 100")
		self.assertEqual(data_type(101), "more than 100")
		self.assertEqual(data_type('julius'), 6)
		self.assertEqual(data_type(True), True)
		self.assertEqual(data_type(False), False)
		self.assertEqual(data_type([1,2,3,4]), 3)
unittest.main()