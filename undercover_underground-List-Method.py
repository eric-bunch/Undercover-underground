def answer(N, K):

	import math
	import itertools
	
	def binom(a, b):
	
		if a < b:
			return 0
		else:
			x = math.factorial(a)
			y = math.factorial(b)
			z = math.factorial(a - b)
			
		div = x // (y*z)
		return div



	def add(u):
		return [ u[0][0]*u[1][0], u[0][1] + u[1][1], u[0][2] + u[1][2] ]



	def mult(s, t):
		
		y = itertools.product(s, t)
		z = itertools.ifilter(lambda x: x[0][2] + x[1][2] <= N, y)
		temp = map(add, z)

		return temp

	def expls_sum(s, t, run_sum, count):

		run_sum += ( (-1)**(count + 1)/float(count) ) * sum( term[0]*binom(term[1], K) for term in t if term[2] == N )
		
		if count == N:
			return run_sum
		else:
			temp = mult(s[:N-count], [term for term in t if term[2] != N])
			return expls_sum(s, temp, run_sum, count + 1)


	summation = [[1/(float(math.factorial(i))), binom(i, 2), i] for i in range(1, N + 1)]
	summ_copy = [[1/(float(math.factorial(i))), binom(i, 2), i] for i in range(1, N + 1)]

	running_sum_x_N = expls_sum(summation, summ_copy, 0, 1)
	
	return str( int( math.factorial(N) * running_sum_x_N ) )

"""
print "N = 2, K = 1: ",answer(2, 1)
print "N = 4, K = 3: ",answer(4, 3)	
print "N = 20, K = 19: ",answer(20, 19)
print "N = 20, K = 50: ",answer(20, 50)
print "N = 20, K = 120: ",answer(20, 120)
"""
