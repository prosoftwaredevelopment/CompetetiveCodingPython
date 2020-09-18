t = int(input())
for i in range(t):
    r,c = map(int,input().split())
    dp = []
    for i in range(r):
        dp.append(list(map(int,input().split())))

    # min cost for row wise
    for i in range(1,r):
        dp[i][0]+=dp[i-1][0]

        
    # min cost for col wise
    for j in range(1,c):
        dp[0][j]+=dp[0][j-1]

    # choice to take min either right or down
    for i in range(1,r):
        for j in range(1,c):
            dp[i][j] += min(dp[i-1][j],dp[i][j-1])
    print(dp[-1][-1])
