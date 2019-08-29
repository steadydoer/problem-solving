# BOJ Coding Test Practice
# 17142: 연구소 3
#
#     https://www.acmicpc.net/problem/17142
#
# ==============================================================================

from collections import deque
from copy import deepcopy
from itertools import combinations


def combine_result(default_state, spread_results, size,
                   virus_locations, total_virus_locations, prev_max):
    current_max = -1
    for r in range(size):
        for c in range(size):
            # not wall and not virus
            if default_state[r][c] != -2 and \
                    (r, c) not in total_virus_locations:
                values = []
                for loc in virus_locations:
                    value = spread_results[loc][r][c]
                    if value > -1:
                        values.append(spread_results[loc][r][c])
                if values:
                    local_min = min(values)
                else:
                    return prev_max
                if current_max < local_min:
                    current_max = local_min
                if prev_max != -1 and current_max > prev_max:
                    return prev_max

    return current_max


def spread_virus(lab, virus):
    row, col = virus
    lab[row][col] = 0
    size = len(lab)
    q = deque()
    q.append(virus)
    while q:
        r, c = q.popleft()
        current_time = lab[r][c]
        next_time = current_time + 1
        if r > 0 and lab[r - 1][c] == -1:
            lab[r - 1][c] = next_time
            q.append((r - 1, c))
        if r + 1 < size and lab[r + 1][c] == -1:
            lab[r + 1][c] = next_time
            q.append((r + 1, c))
        if c > 0 and lab[r][c - 1] == -1:
            lab[r][c - 1] = next_time
            q.append((r, c - 1))
        if c + 1 < size and lab[r][c + 1] == -1:
            lab[r][c + 1] = next_time
            q.append((r, c + 1))
    return lab


def solve():
    n, m = list(map(int, input().split()))
    virus = []
    lab = [[s for s in map(int, input().split())] for _ in range(n)]
    blank = 0
    answer = -1
    default_state = deepcopy(lab)
    for r in range(n):
        for c in range(n):
            state = lab[r][c]
            if state == 0:  # blank
                blank += 1
                default_state[r][c] = -1
            elif state == 2:  # virus
                virus.append((r, c))
                default_state[r][c] = -1
            else:  # wall
                default_state[r][c] = -2

    if blank == 0:
        answer = 0
        return answer

    spread_results = dict()
    for v in virus:
        spread_results[v] = spread_virus(deepcopy(default_state), v)

    for combi in combinations(virus, m):
        answer = combine_result(deepcopy(default_state),
                                spread_results, n, combi, virus, answer)

    return answer


answer = solve()
print(answer)


# if __name__ == '__main__':
#     test_case = int(input())
#
#     # print(test_case)
#     for _ in range(test_case):
#         answer = solve()
#         print(answer)
