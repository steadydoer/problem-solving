# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/43163
#
# ==============================================================================


def bfs(begin, target, words, visited):
    q = [begin]
    level = 0
    while(q):
        qsize = len(q)
        for _ in range(qsize):
            current = q.pop(0)
            for j in range(len(words)):
                if visited[j] is False:
                    layover = words[j]
                    w_len = len(layover)
                    for k in range(w_len):
                        if current[0:k] == layover[0:k] and current[k] != layover[k] and current[k+1:] == layover[k+1:]:
                            visited[j] = True
                            q.append(layover)
        level += 1
        if target in q:
            return level


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    visited = [False for x in range(len(words))]
    answer = bfs(begin, target, words, visited)
    return answer


if __name__ == "__main__":
    assert solution("hit", "cog", ["hot", "dot",
                                   "dog", "lot", "log", "cog"]) == 4
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
