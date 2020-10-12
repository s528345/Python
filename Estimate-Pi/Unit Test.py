#Making tests

import unittest
import Estimate Pi 

class pi10(unittest, TestCase)
	# Test for 10 points
	result = Main.estimate_Pi(10)
	# Check for expected output
	if(2 < result and result < 4):
		resultValue = True
	else:
		resultValue = False

	epected = True
	self.assertEqual(epected,resultValue)

class pi100(unittest, TestCase)
	# Test for 100 points
	result = Main.estimate_Pi(100)
	# Check for expected output
	if(2 < result and result < 4):
		resultValue = True
	else:
		resultValue = False

	epected = True
	self.assertEqual(epected,resultValue)

class pi1000(unittest, TestCase)
	# Test for 1000 points
	result = Main.estimate_Pi(1000)
	# Check for expected output
	if(2 < result and result < 4):
		resultValue = True
	else:
		resultValue = False

	epected = True
	self.assertEqual(epected,resultValue)

class pi10000(unittest, TestCase)
	# Test for 10000 points
	result = Main.estimate_Pi(10000)
	# Check for expected output
	if(2 < result and result < 4):
		resultValue = True
	else:
		resultValue = False

	epected = True
	self.assertEqual(epected,resultValue)
# Run the Tests
if __name__ == '__main__':
	unittest.main()
	