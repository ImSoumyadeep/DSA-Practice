# //Enter code here

from collections import deque

def maxInWindow(a, k, n):
	ans = []
	deq = deque()

	for i in range(k):
		while deq and a[i] >= a[deq[-1]]: deq.pop()
		deq.append(i)

	ans.append(a[deq[0]])

	for i in range(k, n):
		while deq and deq[0] <= i - k: deq.popleft()    
		while deq and a[i] >= a[deq[-1]]: deq.pop()
		deq.append(i)
		ans.append(a[deq[0]])

	return ans



n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = maxInWindow(a, k, n)
for _ in ans: print(_, end = ' ')


