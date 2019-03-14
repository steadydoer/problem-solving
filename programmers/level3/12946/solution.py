# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/12946
#
# ==============================================================================


def hanoi(start, layover, end, n, answer):
    if n == 1:
        answer.append([start, end])
        return
    else:
        hanoi(start, end, layover, n-1, answer)
        answer.append([start, end])
        hanoi(layover, start, end, n-1, answer)
        return


def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer


if __name__ == "__main__":
    assert solution(2) == [[1, 2], [1, 3], [2, 3]]
