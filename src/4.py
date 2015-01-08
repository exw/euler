# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max = 1001

for x in xrange(999):
	for y in xrange(x,999):
		if str(x*y) == str(x*y)[::-1] and x*y > max:
			max = x*y
print max
