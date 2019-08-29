# BOJ Coding Test Practice
# 2628: 종이자르기
#
#     https://www.acmicpc.net/problem/2628
#
# total elapsed time: 18:35 / 54%, 26:35 / 100%
# ==============================================================================

col, row = list(map(int, input().split()))

cols = [col]
rows = [row]
cuts = int(input())
for _ in range(cuts):
    direction, number = list(map(int, input().split()))
    if direction == 0:
        rows.append(number)
    else:
        cols.append(number)

cols.sort()
rows.sort()
widths = [cols[0]]
heights = [rows[0]]
for i in range(len(cols) - 1):
    width = cols[i+1] - cols[i]
    widths.append(width)

for i in range(len(rows) - 1):
    height = rows[i+1] - rows[i]
    heights.append(height)


max_height = max(heights)
max_width = max(widths)
answer = max_height * max_width
print(answer)
