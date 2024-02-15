# Problem link -> https://oj.masaischool.com/contest/10600/problem/04

def generate_parenthesis(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result
    
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    pi = []
    valid_parentheses = generate_parenthesis(n)
    for p in valid_parentheses:
        count +=1
        pi.append(p)
    print(count)
    print(*pi, sep = "\n")
