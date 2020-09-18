# 0 1
# T(n)= T(n-1) + T(n-2)
# T.C = 2^N
# LET N = 10
# RECURSION => TIME COMPLEXITY => O(2^N) = 2^10 = 1024 CAL
# DP => TIME COMPLEXITY => O(N) => 10
# MEMOIZATION IN DP 
'''
def fib(n):
        if n == 0 or n == 1:
                return n
        else:
                return fib(n-1) + fib(n-2)
'''
# GLOBAL LIST FOR ALL TESTCASES
GLOBALFIBDYNAMIC = [0,1]
def fib(n):
        # already computed for previous testcases
        # and now only returning the value
        # since precomputed already
        # no need to compute again
        # memoize
        if n < len(GLOBALFIBDYNAMIC):
                return GLOBALFIBDYNAMIC[n]
        # if not computed
        # then compute the value
        # using memoization
        else:
                for i in range(len(GLOBALFIBDYNAMIC),n+1):
                        last = GLOBALFIBDYNAMIC[-1]
                        secondlast = GLOBALFIBDYNAMIC[-2]
                        GLOBALFIBDYNAMIC.append(last+secondlast)
                return GLOBALFIBDYNAMIC[n]

t = int(input())
for i in range(t):
        N = int(input())
        print(fib(N))
        print(GLOBALFIBDYNAMIC)
