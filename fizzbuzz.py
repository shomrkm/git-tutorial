# -*- coding:utf-8 -*-


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

if __name__=='__main__':

	fb = FizzBuzz()
	for n in range(1,20):
		print "Result : %d -> %s" % ( n, fb.calculate(n) )


