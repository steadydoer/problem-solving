# BOJ Coding Test Practice
# 11559: Puyo Puyo
#
#     https://www.acmicpc.net/problem/11559
#
# ==============================================================================
from collections import deque
from copy import deepcopy


def get_puyos(stage, height, width):
    puyos = set()
    for c in range(width):
        for r in range(height - 1, -1, -1):
            if stage[r][c] == '.':
                break
            else:
                puyos |= {(r, c)}
    return puyos


def refresh_stage(default_stage, current_stage, height, width, chain_puyos):
    next_stage = deepcopy(default_stage)
    for c in range(width):
        cursor = height - 1
        for r in range(height-1, -1, -1):
            if (r, c) not in chain_puyos:
                next_stage[cursor][c] = current_stage[r][c]
                cursor -= 1
            if current_stage[r][c] == '.':
                break

    return next_stage


def solve():
    height = 12
    width = 6
    stage = [[state for state in list(input())] for _ in range(height)]
    default_stage = [['.' for _ in range(width)] for _ in range(height)]
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상

    chain = True
    chain_count = -1
    while chain:
        chain_count += 1
        chain = False
        # 스테이지 기반으로 뿌요 좌표 집합 얻기
        puyos = get_puyos(stage, height, width)
        chain_puyos = set()
        # 모든 뿌요 탐색하기
        while puyos:
            r, c = puyos.pop()
            connected_puyo = set()
            connected_puyo |= {(r, c)}
            q = deque()
            q.append((r, c))
            state = ''
            # 연결된 뿌요 찾기
            while q:
                row, col = q.popleft()
                connected_puyo |= {(row, col)}
                state = stage[row][col]
                for d in directions:
                    diff_row, diff_col = d
                    next_row, next_col = row + diff_row, col + diff_col
                    # 인덱스 범위를 만족하고 다음 지점이 연결된 뿌요에 없고 현재 지점과 다음 지점의 뿌요 상태가 같을 경우
                    if 0 <= next_row < height and 0 <= next_col < width and (next_row, next_col) not in connected_puyo and stage[next_row][next_col] == state:
                        q.append((next_row, next_col))
                        connected_puyo |= {(next_row, next_col)}
            # 연결된 뿌요가 4개 이상일 경우
            if len(connected_puyo) > 3:
                chain = True
                chain_puyos |= connected_puyo
            # 전체 뿌요에서 이번 반복에서 구한 연결 뿌요 제거하기
            puyos -= connected_puyo

        # 스테이지 갱신
        next_stage = refresh_stage(
            default_stage, stage, height, width, chain_puyos)
        stage = next_stage

    return chain_count


answer = solve()
print(answer)
