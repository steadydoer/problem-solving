# Programmers Coding Test Practice
# Level 3 야근지수
#
#     https://programmers.co.kr/learn/courses/30/lessons/12927
#
# ==============================================================================
import heapq


def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        heapq.heappush(hq, -work)
    for i in range(n):
        work = heapq.heappop(hq)
        if work == 0:
            return 0
        heapq.heappush(hq, work + 1)
    for work in hq:
        answer += (work * -1) ** 2

    return answer


if __name__ == '__main__':
    assert solution(4, [4, 3, 3]) == 12
    assert solution(1, [2, 1, 2]) == 6
    assert solution(3, [1, 1]) == 0
