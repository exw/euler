# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

assert problem5(10) == 2520

def problem5(input):
	factors = collectFactors(input)
	answer = product(factors)
	print str(answer)


def collectFactors(arg):
	factors = newDict(arg)
	for x in xrange(2,arg+1):
		gp = getPrimes(x)
		for i in xrange(2,x+1):
			if gp[i] > factors[i]:
				factors[i] = gp[i]
	return factors
	
def getPrimes(i):
	f = newDict(i)
	for x in xrange(2,i+1):
		while i % x == 0:
			f[x] = f[x] + 1
			i = i / x
	return f	

def newDict(i):
	return {key: 0 for key in xrange(2,i+1)}

def product(d):
	answer = 1
	for key,value in d.iteritems():
		answer = answer * (key**value)
	return answer

problem5(20)
