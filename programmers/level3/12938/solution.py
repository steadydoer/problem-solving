# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/12938
#
# ==============================================================================


def solution(n, s):
    if n > s:
        return [-1]
    default = s // n
    answer = [default for x in range(n)]
    for i in range(n*default, s):
        answer[i % n] += 1
    answer.sort()
    return answer


if __name__ == "__main__":
    assert solution(2, 9) == [4, 5]
    assert solution(2, 1) == [-1]
