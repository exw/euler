import sys

def problem8(input):
	raw = sys.stdin.read().split('0')
	max = 1
	targets = [target for target in raw if len(target) >= input]
	print targets
	for target in targets:
		index = 0
		for start in xrange(len(target)-input+1):
			product = 1
			for each in target[index:index+input:1]:
				product = product * int(each)
			if max < product:
				max = product
			index = index + 1
	print str(max)		

problem8(13)

