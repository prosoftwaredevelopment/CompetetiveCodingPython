# ispowerof 2
# n -> input
# True/False -> output
# check if n is a powerof 2
# 512 -> True 512 = 2**9
# 1024 -> True 1024 = 2**10

def ispowerof2(n):
    # T.C = O(1)
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y

# return's number of 1's in binary representation of int
# 5 -> 101 ans = 2
# 7 -> 111 ans = 3

def bruteforcecntbits(n):
    # T.C = O(n)
    s = str(bin(n))[2:]
    print("{}".format(s))
    return s.count('1')


def cntbits(n):
    # T.C = O(logn)
    cnt = 0
    while n:
        cnt+=1
        n = n & (n-1)
    return cnt



t= int(input())
while t:
    n = int(input())
    #print(ispowerof2(n))
    print(bruteforcecntbits(n))
    print(cntbits(n))
    t=t-1
