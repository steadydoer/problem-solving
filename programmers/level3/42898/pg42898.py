# Programmers Coding Test Practice
# Level 3 등굣길
#
#     https://programmers.co.kr/learn/courses/30/lessons/42898
#
# ==============================================================================


def solution(m, n, puddles):
    ways = [[0] * (m + 1) for _ in range(n + 1)]
    ways[0][1] = 1
    ways[1][0] = 1
    puddles = {tuple(puddle): 1 for puddle in puddles}
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if (col, row) in puddles:
                ways[row][col] = 0
                continue
            if row == 1:
                ways[row][col] = ways[row][col - 1]
                continue
            if col == 1:
                ways[row][col] = ways[row - 1][col]
                continue
            ways[row][col] = (ways[row - 1][col] + ways[row][col - 1]) % 1000000007
    answer = ways[n][m]
    return answer


if __name__ == '__main__':
    assert solution(4, 3, [[2, 2]]) == 4
