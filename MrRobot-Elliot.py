# Problem link -> https://oj.masaischool.com/contest/10656/problem/02

# //Enter code here

def recursion(s, start, end):
	if start > end: return
	mid = (start + end) // 2;
	print(s[mid], end = "")
	recursion(s, start, mid-1)
	recursion(s, mid + 1, end)

for _ in range(int(input())):
    n = int(input())
    s = input()
    recursion(s, 0, n-1)
    print()
