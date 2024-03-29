# //Enter code here

def mostWater(a, n):
	l, r, ans = 0, n-1, 0
	while l < r:
		ans = max(ans, min(a[l], a[r]) * (r-l))     
		if a[l] < a[r]: l += 1
		else: r -= 1
	return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(mostWater(a, n))

