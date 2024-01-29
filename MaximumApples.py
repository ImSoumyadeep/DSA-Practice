
# Code link - https://oj.masaischool.com/contest/10958/problem/01

n, k = map(int, input().split())
w = list(map(int, input().split()))
w.sort()

wt, ans = 0, 0
for i in w:
    wt += i
    if wt <= k: ans += 1
    else: break

print(ans)
