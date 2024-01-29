
# Code link - https://oj.masaischool.com/contest/10958/problem/02

def process(a):
    for i in range(len(a)):
        hr, mi = map(int, a[i].split(":"))
        a[i] = hr * 100 + mi
    return sorted(a)
    
n = int(input())
arr = list(input().split())
dep = list(input().split())

arr, dep = process(arr), process(dep)
pf, ans, i, j = 1, 1, 1, 0

while i < n and j < n:
	if arr[i] <= dep[j]: pf += 1; i += 1
	elif arr[i] > dep[j]: pf -= 1; j += 1

	if pf > ans: ans = pf

print(ans)

