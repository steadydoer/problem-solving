# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/12985
#
# ==============================================================================


def solution(n, a, b):
    answer = 1

    if a > b:
        a, b = b, a
    while b - a != 1:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    while a % 2 == 0:
        a = a // 2
        answer += 1

    return answer


if __name__ == '__main__':
    assert solution(8, 4, 7) == 3
