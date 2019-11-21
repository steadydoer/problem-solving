# BOJ Coding Test Practice
# 3108: 로고
#
#     https://www.acmicpc.net/problem/3108
#
# total elapsed time: 18:35 / 54%, 26:35 / 100%
# ==============================================================================


def get_points(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    points = set()
    for x in range(x1, x2):
        points.add((x, y1))
    for x in range(x2, x1, -1):
        points.add((x, y2))
    for y in range(y1, y2):
        points.add((x2, y))
    for y in range(y2, y1, -1):
        points.add((x1, y))

    return points


def solve():
    answer = 0
    cnt = int(input())
    rectangles = [[point for point in map(
        int, input().split())] for _ in range(cnt)]
    points_list = []
    zero_start = False
    for x1, y1, x2, y2 in rectangles:
        points = get_points(x1, y1, x2, y2)
        if (0, 0) in points:
            zero_start = True
        points_list.append(points)

    groups = [points_list[0]]
    for i in range(1, len(points_list)):
        for j in range(len(groups)):
            if groups[j] & points_list[i]:
                groups[j] |= points_list[i]
                break
        else:
            groups.append(points_list[i])

    answer = len(groups)
    if zero_start:
        answer -= 1
    return answer


answer = solve()
print(answer)
