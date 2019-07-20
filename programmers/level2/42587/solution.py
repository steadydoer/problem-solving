# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/42587
#
# ==============================================================================
import queue
from collections import deque


def solution(priorities, location):
    enum = list(enumerate([-x for x in priorities]))  # (location, -priority)
    normal_q = deque(enum)
    pq = queue.PriorityQueue()
    # put (-priority, location)
    for item in enum:
        pq.put((item[1], item[0]))
        pass
    result = {}
    order = 1

    while(normal_q):
        item = normal_q.popleft()
        p_item = pq.get()
        if item[1] > p_item[0]:  # ex: -1 > -9
            normal_q.append(item)
            pq.put(p_item)
        else:
            result[item[0]] = order
            order += 1

    answer = result.get(location)
    return answer


if __name__ == "__main__":
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
