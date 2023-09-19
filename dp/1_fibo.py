# everyones fav dp starter - fibo

# Using Memoization
def fibo(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1: return dp[n]

    dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

n = 10
dp = [-1]*(n+1)
fibo(n, dp)
print(dp)


# using tabulation (bottom up)
n = 10
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp)

# space optimized
n = 10
first = 0
sec = 1
for _ in range(2, n+1):
    curr = first + sec
    first = sec
    sec = curr
print(curr)