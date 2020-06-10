# Programmers Coding Test Practice
# Level 3 기지국 설치
#
#     https://programmers.co.kr/learn/courses/30/lessons/12979
#
# ==============================================================================
from math import ceil


def solution(n, stations, w):
    answer = 0
    stations.append(n + w + 1)
    max_wave_range = w * 2 + 1
    start = 1
    for station in stations:
        if n < start:
            break
        end = station - w
        if start < end:
            answer += ceil((end - start) / max_wave_range)
        start = station + w + 1

    return answer


if __name__ == '__main__':
    assert solution(11, [4, 11], 1) == 3
    assert solution(16, [9], 2) == 3
