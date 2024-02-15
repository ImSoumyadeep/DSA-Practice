# Problem link -> https://oj.masaischool.com/contest/10600/problem/03

# //Enter code here

def fun(virat, rohit, n, m):
    prev, cur = [0] * (m+1), [0] * (m+1)
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if virat[i - 1] == rohit[j - 1]: cur[j] = 1 + prev[j - 1]
            else: cur[j] = max(cur[j - 1], prev[j])
        prev = cur.copy()
 
    return cur[m]

virat = input()
rohit = input()
print(fun(virat, rohit, len(virat), len(rohit)))
