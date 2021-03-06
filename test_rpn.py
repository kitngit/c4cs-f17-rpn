#!/usr/bin/python
import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)

	def test_sub(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)

	def test_mul(self):
		result = rpn.calculate('2 1 *')
		self.assertEqual(2, result)
	
	def test_div(self):
		result = rpn.calculate('8 4 /')
		self.assertEqual(2, result)
	def test_exponent(self):
		result = rpn.calculate('2 4 ^')
		self.assertEqual(16, result)
