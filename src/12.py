def triangle(i):
    return i*(i+1)/2


def countFactors(i):
    factors = 1
    for x in xrange(1, (i/2)+1):
        if (i % x == 0):
            factors += 1
    return factors

def divisorBound(i):
    d=0
    ans=0
    while (d<i):
        ans += 1
        d = countFactors(ans)
    return ans

if (__name__ == "__main__"):
    print divisorBound(10)
    print divisorBound(500)
