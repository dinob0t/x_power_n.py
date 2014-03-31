""" 
Algorithm to calculate x^n where n is an integer
Note x^n =  | x(x^2)(n-1)/2 if n is odd
			| (x^2)^(n/2) if n is even
Exponential squaring improves run time by ~ factor of 2
"""
import time
n = -2
x = 3


def x_n_squaring(x,n):
	if n<0:
		return x_n_squaring(1.0/x, -n)
	elif n==0:
		return 1
	elif n==1:
		return x
	elif n%2==0:
		return x_n_squaring(x*x,n/2)
	elif n%2==1:
		return x*x_n_squaring(x*x,(n-1)/2)


t0 = time.time()
print "x^n calculated directly is  %f" %x**n
t1 = time.time()
print "Time taken %f s" %(t1-t0)

t0 = time.time()
print "x^n calculated by squaring is  %f" %x_n_squaring(x,n)
t1 = time.time()
print "Time taken %f s" %(t1-t0)






