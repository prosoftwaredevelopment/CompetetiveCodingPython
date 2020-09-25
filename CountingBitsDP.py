'''
Problem Statement:
**INTERVIEW QUESTION**
For i = 0 to N 
return a list of number of one's in binary representation of i
5
[0,1,1,2,1,2]
(0)000 -> 0
(1)001 -> 1
(2)010 -> 1
(3)011 -> 2
(4)100 -> 1
(5)101 -> 2
'''
# TIME COMPLEXITY = O(N^2)  => N FOR LOOP * N FOR .count() = N*N = N^2
def approach1(n):
	res = []
	for i in range(n+1):
		binary = bin(i)[2:]
		res.append(binary.count('1'))
	return res


def cntone(x):
	cnt = 0
	while x:
		cnt+=1
		x = x & (x-1)
	return cnt

# TIME COMPLEXITY = O(NLOGN) => N FOR LOOP * LOGN FOR CNTONE = N*LOGN = NLOGN
def approach2(n):
	res = []
	for i in range(n+1):
		res.append(cntone(i))
	return res


# TIME COMPLEXITY = O(N) => FOR LOOP ONLY
def approach3(n):
	res = []
	res = [0]
	for i in range(1,n+1):
		res.append(res[i//2]+i%2)
	return res

N = 5
print(approach1(N))
print(approach2(N))
print(approach3(N))