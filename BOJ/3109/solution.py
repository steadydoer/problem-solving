# BOJ Coding Test Practice
# 3109: 빵집
#
#     https://www.acmicpc.net/problem/3109
#
# ==============================================================================


def solve():
    answer = 0
    row, col = list(map(int, input().split()))
    grid = [[state for state in list(input())] for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    directions = [(-1, 1), (0, 1), (1, 1)]

    def dfs(y, x):
        nonlocal row
        nonlocal col
        nonlocal visited
        visited[y][x] = 1
        if x == col - 1:
            return True

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < row and 0 <= nx < col:
                if not visited[ny][nx] and grid[ny][nx] == '.':
                    if dfs(ny, nx):
                        return True

        return False

    for y in range(row):
        if dfs(y, 0):
            answer += 1

    return answer


answer = solve()
print(answer)
