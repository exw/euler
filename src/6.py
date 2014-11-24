def problem6(input):
  sumOfSquares = 0
  squareOfSums = 0
  for x in xrange(input+1):
    sumOfSquares = sumOfSquares + x**2
    squareOfSums = squareOfSums + x
  answer = abs(squareOfSums**2 - sumOfSquares)
  print answer
 
problem6(10)
problem6(100)
