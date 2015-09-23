# -*- coding:utf-8 -*-

import unittest


class FizzBuzz:

	def calculate( self, number ):
		if number%3 == 0 and number%5 == 0:
			return "fizzbuzz"

		if number%3 == 0:
			return "fizz"

		if number%5 == 0:
			return "buzz"
              
		if '7' in str(number):
			return "GitHub"

		else:
			return number


class TestFizzBuzz(unittest.TestCase):

	def test_calculate(self):

		fb = FizzBuzz()
		self.assertEqual(fb.calculate(1)  ,1)
		self.assertEqual(fb.calculate(3)  ,"fizz")
		self.assertEqual(fb.calculate(5)  ,"buzz")
		self.assertEqual(fb.calculate(15) ,"fizzbuzz")
		self.assertEqual(fb.calculate(17) ,"GitHub")


if __name__=='__main__':
	unittest.main()


