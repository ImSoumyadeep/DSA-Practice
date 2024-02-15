# Problem link -> https://oj.masaischool.com/contest/10656/problem/03

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def solve(head):
    # Write code here
    ans, i = "YES", 1
    
    while head != None:
        if i % 2 == 0: 
            if head.data % 2 != 1: ans = "NO"
        else:
            if head.data % 2 != 0: ans = "NO"
        
        i += 1;     head = head.next
    
    return ans
