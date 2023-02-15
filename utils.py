from math import sqrt
from scipy import integrate as itg

def fact(n):
	if n < 2:
		return 1
	else:
		return n*fact(n-1)


def roots(a, b, c):
	d=b*b-4*a*c
	if d>0:
 		return [(-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a)]
	elif d == 0 : 
		return -b/2*a

def integrate(function, lower, upper):
	result = itg.quad(lambda x : eval(function), lower, upper)
	return result[0]

if __name__=='__main__' : 

	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
