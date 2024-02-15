# Problem link -> https://oj.masaischool.com/contest/10656/problem/04

# //Enter code here

def fun(a, n):
	dp, ans, i = [0 for i in range(n+2)], 0, n-1

	while i >= 0:
		if i + a[i] >= n: dp[i] = a[i]
		else: dp[i] = dp[i + a[i]] + a[i]

		ans = max(ans, dp[i]);      i -= 1
	print(ans)

n = int(input())
a = list(map(int, input().split()))
fun(a, n)
