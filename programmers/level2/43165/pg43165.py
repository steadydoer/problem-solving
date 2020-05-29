# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/43165
#
# ==============================================================================
from collections import deque


def solution(numbers, target):
    answer = 0
    end = len(numbers)
    dq = deque()
    dq.append([0, 0])
    while dq:
        total, idx = dq.popleft()
        if idx == end:
            if total == target:
                answer += 1
            continue
        dq.append([total + numbers[idx], idx + 1])
        dq.append([total - numbers[idx], idx + 1])

    return answer


if __name__ == '__main__':
    assert solution([1, 1, 1, 1, 1], 3) == 5
