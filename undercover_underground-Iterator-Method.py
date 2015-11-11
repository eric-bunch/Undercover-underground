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
		temp = itertools.imap(add, z)
					
		return temp

	def expls_sum(s, t, run_sum, count):
		
		t_temp_iter1, t_temp_iter2 = itertools.tee(t)

		run_sum += ( (-1)**(count + 1)/float(count) ) * sum( term[0]*binom(term[1], K) for term in t_temp_iter1 if term[2] == N )
		
		s_temp_iter1, s_temp_iter2 = itertools.tee(s)
		
		if count == N:
			return run_sum
		else:

			temp = mult(itertools.ifilter(lambda x: x[2] <= N - count, s_temp_iter1), 
											itertools.ifilter(lambda x: x[2] != N, t_temp_iter2))
			
			return expls_sum(s_temp_iter2, temp, run_sum, count + 1)


	sum_list = [[1/(float(math.factorial(i))), binom(i, 2), i] for i in range(1, N + 1)]
	sum_gen = ([1/(float(math.factorial(i))), binom(i, 2), i] for i in range(1, N + 1))

	x_N_coeff = expls_sum(sum_list, sum_gen, 0, 1)
	
	return str( int( math.factorial(N) * x_N_coeff ) )

"""
print "N = 2, K = 1: ",answer(2, 1)
print "N = 4, K = 3: ",answer(4, 3)	
print "N = 20, K = 19: ",answer(20, 19)
print "N = 20, K = 50: ",answer(20, 50)
print "N = 20, K = 120: ",answer(20, 120)
"""
