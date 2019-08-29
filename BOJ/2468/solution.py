# BOJ Coding Test Practice
# 2468: 안전 영역
#
#     https://www.acmicpc.net/problem/2468
#
# total elapsed time: 80:15
# ==============================================================================
from collections import deque
from copy import deepcopy

n = int(input())
area = [[h for h in list(map(int, input().split()))] for _ in range(n)]
sinks = [[0]*(n) for _ in range(n)]
heights = set()
for row in area:
    heights |= set(row)
heights = list(heights)
heights.append(0)
heights.sort()
answer = -1
for h in heights:
    temp_sinks = deepcopy(sinks)
    q = deque()
    for r in range(n):
        for c in range(n):
            if area[r][c] <= h:
                temp_sinks[r][c] = 1

    count_ = 0
    for r in range(n):
        for c in range(n):
            if not temp_sinks[r][c]:
                count_ += 1
                q.append((r, c))
                temp_sinks[r][c] = 1
                while q:
                    current_row, current_col = q.popleft()

                    if current_row > 0 and not temp_sinks[current_row - 1][current_col]:
                        q.append((current_row - 1, current_col))
                        temp_sinks[current_row - 1][current_col] = 1
                    if current_row + 1 < n and not temp_sinks[current_row + 1][current_col]:
                        q.append((current_row + 1, current_col))
                        temp_sinks[current_row + 1][current_col] = 1
                    if current_col > 0 and not temp_sinks[current_row][current_col - 1]:
                        q.append((current_row, current_col - 1))
                        temp_sinks[current_row][current_col - 1] = 1
                    if current_col + 1 < n and not temp_sinks[current_row][current_col + 1]:
                        q.append((current_row, current_col + 1))
                        temp_sinks[current_row][current_col + 1] = 1
    if answer < count_:
        answer = count_

print(answer)
