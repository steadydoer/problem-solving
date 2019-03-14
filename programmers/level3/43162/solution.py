# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/43162
#
# ==============================================================================
from collections import deque


def bfs(n, start, computers, visited):
    visited[start] = True
    q = deque([start])
    while(q):
        current = q.popleft()
        adj = computers[current]
        for i in range(n):
            if i == current:
                continue
            if visited[i] is False and adj[i] == 1:
                visited[i] = True
                q.append(i)


def solution(n, computers):
    answer = 0
    visited = [False for x in range(n)]
    for i in range(n):
        if visited[i] is False:
            bfs(n, i, computers, visited)
            answer += 1
    return answer


if __name__ == "__main__":
    assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
