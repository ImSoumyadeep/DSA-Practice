# //Enter code here

# Code link - https://oj.masaischool.com/contest/10958/problem/03

n = int(input())
w = list(map(int, input().split()))

i, lsum = 1, 0
while lsum + i <= n:
    lsum += i
    i += 1

print(i-1)
