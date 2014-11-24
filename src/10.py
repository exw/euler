import math
import numpy
def primeList(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)
  
  
def problem10:
answer = sum(primeList(2000000))

print answer
