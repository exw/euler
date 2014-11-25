import sys

checkSize = 4

raw = sys.stdin.readlines()
graph = []
for line in raw:
	graph.append(line.strip('\n').split(' '))



def horizmax():
	max = 0
	for row in graph:
		for i in xrange(len(row) - checkSize):
			x = 0
			product = 1
			while x < checkSize:
				product = product * long(row[i+x])
				print product
				x = x+1
			if product > max:
				max = product
	return max

def vertmax():
	max = 0
	for j in xrange(len(graph) - checkSize):
		i = 0
		for column in graph[j]:
			y = 0
			product = 1
			while y < checkSize:
				product = product * long(graph[j+y][i])
			

