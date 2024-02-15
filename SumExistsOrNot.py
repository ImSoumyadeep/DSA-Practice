# Problem link -> https://oj.masaischool.com/contest/10656/problem/01

def isSubsetSum(nums, target_sum):
    n = len(nums)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # An empty subset can always have a sum of 0
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the sum, it cannot be included
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Check if either including the current element or excluding it gives the desired sum
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # The final result is stored in the bottom-right cell of the dp matrix
    return dp[n][target_sum]

# Example usage
n = int(input())
nums = list(map(int,input().split()))
target_sum = int(input())
if isSubsetSum(nums, target_sum):
    print("yes")
else:
    print("no")
