
# Code link - https://oj.masaischool.com/contest/10958/problem/05

n = int(input())
vc = list(map(int, input().split()))
mc = list(map(int, input().split()))

mc.sort();  vc.sort();  ans = "Yes"
for i in range(n):
    if mc[i] > vc[i]: ans = "No"

print(ans)
