# Programmers Coding Test Practice
# Level 3 숫자 게임
#
#     https://programmers.co.kr/learn/courses/30/lessons/12987
#
# ==============================================================================


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_idx = 0
    for b in B:
        if b <= A[a_idx]:
            continue
        answer += 1
        a_idx += 1
    return answer


if __name__ == '__main__':
    assert solution([5, 1, 3, 7], [2, 2, 6, 8]) == 3
    assert solution([2, 2, 2, 2], [1, 1, 1, 1]) == 0
