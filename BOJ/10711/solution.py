# BOJ Coding Test Practice
# 10711: 모래성
#
#     https://www.acmicpc.net/problem/10711
#
# ==============================================================================
from collections import deque

# 초기 풀이법
# def solve():
#     answer = 0
#     directions = ((-1, 0), (-1, 1), (0, 1), (1, 1),
#                   (1, 0), (1, -1), (0, -1), (-1, -1))
#     h, w = list(map(int, input().split()))
#     sand_castle = []
#     fragile_sand = set()
#     broken_sand = set()
#     waves = dict()
#     blank = set()
#     for r in range(h):
#         line = list(input())
#         row = []
#         for c in range(w):
#             elem = line[c]
#             if elem == '.':
#                 row.append(10)
#                 blank |= {(r, c)}
#             else:
#                 firmness = int(elem)
#                 row.append(firmness)
#                 if firmness < 9:
#                     fragile_sand |= {(r, c)}
#         sand_castle.append(row)

#     broken_sand = set()
#     for loc in fragile_sand:
#         r, c = loc
#         firmness = sand_castle[r][c]
#         wave = 0
#         for diff_r, diff_c in directions:
#             next_row, next_col = r + diff_r, c + diff_c
#             if (next_row, next_col) in blank:
#                 wave += 1
#             if wave >= firmness:
#                 broken_sand |= {loc}
#                 break
#         waves[(r, c)] = wave
#     fragile_sand -= broken_sand

#     while broken_sand:
#         answer += 1
#         next_broken_sand = set()
#         for loc in broken_sand:
#             r, c = loc
#             for diff_r, diff_c in directions:
#                 next_row, next_col = r + diff_r, c + diff_c
#                 if (next_row, next_col) in fragile_sand:
#                     firmness = sand_castle[next_row][next_col]
#                     waves[(next_row, next_col)] += 1
#                     if waves[(next_row, next_col)] >= firmness:
#                         next_broken_sand |= {(next_row, next_col)}
#                         fragile_sand -= {(next_row, next_col)}

#         broken_sand = next_broken_sand

#     return answer


def get_wave(sand_castle, r, c, h, w, directions):
    wave = 0
    for diff_r, diff_c in directions:
        if 0 <= r + diff_r < h and 0 <= c + diff_c < w:
            if sand_castle[r + diff_r][c + diff_c] == 0:
                wave += 1
    return wave


# 개선된 풀이법
def solve():
    answer = -1
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1))
    h, w = map(int, input().split())
    sand_castle = []
    waves = []
    fragile_sand = deque()
    for _ in range(h):
        sand_castle.append(list(map(int, list(input().replace('.', '0')))))

    for r in range(h):
        wave_row = []
        for c in range(w):
            if 0 < sand_castle[r][c] < 9:
                fragile_sand.append((r, c))
            wave = get_wave(sand_castle, r, c, h, w, directions)
            wave_row.append(wave)
        waves.append(wave_row)
    broken = True
    broken_sand = deque()
    while broken:
        answer += 1
        broken = False
        next_broken_sand = deque()

        while fragile_sand:
            r, c = fragile_sand.popleft()
            # 파도 >=  모래 강도
            if waves[r][c] >= sand_castle[r][c]:
                broken_sand.append((r, c))

        if broken_sand:
            broken = True

        for r, c in broken_sand:
            sand_castle[r][c] = 0

        while broken_sand:
            r, c = broken_sand.popleft()
            for diff_r, diff_c in directions:
                if 0 <= r + diff_r < h and 0 <= c + diff_c < w:
                    waves[r + diff_r][c + diff_c] += 1
                    if 0 < sand_castle[r + diff_r][c + diff_c] < 9:
                        if waves[r + diff_r][c + diff_c] == sand_castle[r + diff_r][c + diff_c]:
                            next_broken_sand.append((r + diff_r, c + diff_c))

        broken_sand = next_broken_sand

    return answer


answer = solve()
print(answer)
