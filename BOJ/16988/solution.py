# BOJ Coding Test Practice
# 16988: Baaaaaaaaaduk2 (Easy)
#
#     https://www.acmicpc.net/problem/16988
#
# ==============================================================================
from collections import deque
from copy import deepcopy


def combine_group(group_one, group_two):
    combined_group = deepcopy(group_two)
    for blank_locations, stones in group_two.items():
        add = 0
        for blank in blank_locations:
            if blank in group_one:
                add += group_one[blank]
        combined_group[blank_locations] = stones + add

    return combined_group


def solve():
    answer = 0
    # 상 우 하 좌
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    n, m = map(int, input().split())
    plate = [[s for s in map(int, input().split())] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    group_one = {}
    group_two = {}
    for r in range(n):
        for c in range(m):
            if not visit[r][c] and plate[r][c] == 2:
                count_ = 0
                visit[r][c] = 1
                q.append((r, c))
                count_ += 1
                blanks = set()
                while q:
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc]:
                            state = plate[nr][nc]
                            if state == 2:
                                visit[nr][nc] = 1
                                q.append((nr, nc))
                                count_ += 1
                            if state == 0:
                                blanks |= {(nr, nc)}
                if len(blanks) < 3:
                    blanks = tuple(sorted(list(blanks)))
                    if len(blanks) == 1:
                        blanks = blanks[-1]
                        group_one[blanks] = group_one.get(blanks, 0) + count_
                    elif len(blanks) == 2:
                        group_two[blanks] = group_two.get(blanks, 0) + count_
    group_two = combine_group(group_one, group_two)
    values = [[0] for _ in range(3)]
    if group_one:
        for stones in group_one.values():
            values[1].append(stones)
    if group_two:
        for stones in group_two.values():
            values[2].append(stones)
    for sub in values:
        sub.sort()
    one = sum(values[1][-2:])
    two = values[2][-1]
    if one > two:
        answer = one
    else:
        answer = two

    return answer


answer = solve()
print(answer)
