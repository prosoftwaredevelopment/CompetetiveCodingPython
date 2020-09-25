def solvedp(A,n):

	# if we have only one value to steal
	if n == 1:
		return A[0]

	# if we have only two values to steal then select max of either two
	if n == 2:
		return max(A)

	# else use dp to compute optimal soln
	# you want to start with a max value , so you steal the first house or second house
	A[1] = max(A[0],A[1])
	# you have a choice
	# to steal in the previous house / steal in the current house and one house apart from it 
	for i in range(2,n):
		A[i] = max(A[i-1],A[i]+A[i-2])

	# return the last value since it is the sum of all maximum possible stolen values
	return A[-1]


firstestcase = [6, 7, 1, 3, 8, 2, 4]
# 19
# 6->1->8->4
secondtestcase = [5, 3, 4, 11, 2]
# 16
# 5->11
print(solvedp(firstestcase,len(firstestcase)))
print(solvedp(secondtestcase,len(secondtestcase)))