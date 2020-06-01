# Programmers Coding Test Practice
# Level 3 줄 서는 방법
#
#     https://programmers.co.kr/learn/courses/30/lessons/12936
#
# ==============================================================================


def solution(n, k):
    answer = []
    elements = [i + 1 for i in range(n)]
    k = k - 1
    factorial = [1]
    for i in range(1, n+1):
        factorial.append(factorial[-1] * i)
    while elements:
        if len(elements) == 1:
            answer.append(elements.pop())
            break
        divider = factorial[len(elements) - 1]
        answer.append(elements.pop(elements.index(elements[k // divider])))
        k = k % divider
    return answer


if __name__ == '__main__':
    assert solution(3, 5) == [3, 1, 2]
