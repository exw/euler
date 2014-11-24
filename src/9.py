def problem9(sum):
	for a in xrange(1,sum):
		for b in xrange(a,sum-a):
			c = sum - a - b
			if a**2 + b**2 == c**2:
				answer = a * b * c
				print a,b,c
				print str(answer)

problem9(12)
problem9(1000)
