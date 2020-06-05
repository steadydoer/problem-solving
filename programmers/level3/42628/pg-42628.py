# Programmers Coding Test Practice
# Level 3 이중우선순위큐
#
#     https://programmers.co.kr/learn/courses/30/lessons/42628
#
# ==============================================================================
import heapq


def solution(operations):
    min_hq = []
    max_hq = []
    for operation in operations:
        command, value = operation.split(' ')
        value = int(value)
        if command == 'I':
            heapq.heappush(min_hq, value)
            heapq.heappush(max_hq, -value)
        elif command == 'D':
            if not min_hq:
                continue
            if value == 1:
                max_ = -heapq.heappop(max_hq)
                min_hq.remove(max_)
                heapq.heapify(min_hq)
            elif value == -1:
                min_ = -heapq.heappop(min_hq)
                max_hq.remove(min_)
                heapq.heapify(max_hq)
    if min_hq:
        answer = [-heapq.heappop(max_hq), heapq.heappop(min_hq)]
    else:
        answer = [0, 0]
    return answer


if __name__ == '__main__':
    assert solution(['I 16', 'D 1']) == [0, 0]
    assert solution(['I 7', 'I 5', 'I -5', 'D -1']) == [7, 5]
