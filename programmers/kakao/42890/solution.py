# Programmers Coding Test Practice
# 2019 KAKAO BLIND RECRUITMENT 후보키
#
#     https://programmers.co.kr/learn/courses/30/lessons/42890
#
# ==============================================================================
from collections import deque
from itertools import combinations


def check_candidate(*args):
    check_list = list()
    check_set = set()
    for t in zip(*args):
        check_list.append(t)
        check_set |= {t}

    if len(check_list) == len(check_set):
        return True
    else:
        return False


def make_args(indicies, columns):
    args = []
    for idx in indicies:
        args.append(columns[idx])
    return args


def solution(relation):
    answer = 0
    column = len(relation[0])
    row = len(relation)
    col_idx = set(range(column))
    columns = [[] for _ in range(column)]
    for r in range(row):
        for c in range(column):
            columns[c].append(relation[r][c])

    run = True
    combi_size = 1
    while run:
        run = False
        delete = set()
        if combi_size > len(col_idx):
            break
        for indicies in combinations(col_idx, combi_size):
            args = make_args(indicies, columns)
            if check_candidate(*args):
                answer += 1
                delete |= {idx for idx in indicies}
                run = True
        combi_size += 1
        col_idx -= delete

    return answer


if __name__ == '__main__':
    assert solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
                    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]) == 2
