# Programmers Coding Test Practice
# Level 2 라면공장
#
#     https://programmers.co.kr/learn/courses/30/lessons/42629
#
# ==============================================================================
from collections import deque
import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    dq = deque()
    for date, supply in zip(dates, supplies):
        dq.append((date, supply))
    hq = []
    while dq:
        if k <= stock:
            break
        date, supply = dq.popleft()
        if stock < date:
            dq.appendleft((date, supply))
            while stock <= date:
                stock -= heapq.heappop(hq)
                answer += 1
            continue
        heapq.heappush(hq, (-supply))

    while stock < k:
        stock -= heapq.heappop(hq)
        answer += 1
    return answer


if __name__ == '__main__':
    # assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2
    assert solution(4, [1, 2, 3, 4], [1, 1, 1, 1], 6) == 2
