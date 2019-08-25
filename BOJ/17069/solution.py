# BOJ Coding Test Practice
# 17069: 파이프 옮기기 2
#
#     https://www.acmicpc.net/problem/17069
#
# total elapsed time: 78:45
# ==============================================================================
n = int(input())
house = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n + 1)] for _ in range(n+1)]  # n+1 x n+1 x n+1

# row, col, direction;
# direction; 0:horizontal, 1:vertical, 2:diagonal
dp[1][2][0] = 1
for row in range(1, n+1):
    for col in range(1, n+1):
        if col < n and not house[row][col+1]:
            dp[row][col+1][0] += dp[row][col][0] + dp[row][col][2]
        if row < n and not house[row+1][col]:
            dp[row+1][col][1] += dp[row][col][1] + dp[row][col][2]
        if col < n and row < n and not (house[row][col+1] + house[row+1][col] + house[row+1][col+1]):
            dp[row+1][col+1][2] += dp[row][col][0] + \
                dp[row][col][1] + dp[row][col][2]

print(sum(dp[n][n]))
