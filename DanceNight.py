# //Enter code here

# Code link - https://oj.masaischool.com/contest/10958/problem/04

for _ in range(int(input())):
    m, n = map(int, input().split())
    
    hb = list(map(int, input().split()))
    hg = list(map(int, input().split()))
    
    if m > n: print("NO")
    else:
        hb.sort();  hg.sort()
        ans = "YES"
        for i in range(m):
            if hg[i] >= hb[i]: ans = "NO";  break
        print(ans)
