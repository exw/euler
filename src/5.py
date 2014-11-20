def problem5(input):
	d = collectFactors(input)
	answer = product(d)
	print str(answer)


def collectFactors(i):
	factors = newDict(i)
	for x in xrange(i):
		factors = newFactors(factors, getPrimes(x))
	return factors
	
def getPrimes(i):
	f = newDict(i)
	r = xrange(i)
	for x in :
		while i % x == 0:
			f[x] = f[x] + 1
			i = i / x
	return f	
	
def newFactors(answer,new):
	print answer,new
	for key,value in new:
		print "why dont this work"
		if answer[key] < value:
			answer[key] = value
	print answer
	return answer

def newDict(i): 
	return {key: 0 for key in xrange(i)}

def product(d):
	print "p ok"
	answer = 1
	for key,value in d:
		answer = answer * (key**value)
	return answer

problem5(10)
	
