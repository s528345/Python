# Unit Testing
# Testing Python-Sudoku-Solver Main.py

import unittest
import Main 

class goodBoard(unittest, TestCase)
	# Test solvable boards
	result = Main.solve_board(board)
	# Check for expected output
	epected = True
	self.assertEqual(epected,resultEmpty)

class badBoard(unittest, TestCase)
	# Test for bad boards
	result = Main.solve_board(board2)
	# Check for expected output
	epected = False
	self.assertEqual(epected,resultEmpty)

# Run the Tests
if __name__ == '__main__':
	unittest.main()