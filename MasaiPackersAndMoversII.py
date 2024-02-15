# Problem link -> https://oj.masaischool.com/contest/10600/problem/02

# //Enter code here

def recursion(i, n, current_wt, req_wt, cap, day, maax, miin):
    if i == n or current_wt > req_wt: return [maax, miin]
    if current_wt == req_wt:
        maax = max(day, maax)
        miin = min(day, miin)
        return [maax, miin]
    
    [maax, miin] = recursion(i, n, current_wt+cap[i], req_wt, cap, day+1, maax, miin)
    [maax, miin] = recursion(i+1, n, current_wt, req_wt, cap, day, maax, miin)
    
    return [maax, miin]
    
w, n = map(int, input().split())

cap = list(map(int, input().split()))
cap.sort()

maax, miin = -1, 99999
for i in range(n):
    [maax, miin] = recursion(i, n, 0, w, cap, 0, maax, miin)

if maax == -1: print(maax)
else: print(miin, maax)
