# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/12899
#
# ==============================================================================


def solution(n):
    answer = ''
    numbers = ['1', '2', '4']
    order = 0
    bound = 0
    boundaries = [0]
    while(bound < n):
        order += 1
        bound += 3 ** order
        boundaries.append(bound)

    for i in range(order-1, 0, -1):
        divisor = 3 ** i
        quotitent = int((n - boundaries[i] - 1) / divisor)
        answer += numbers[quotitent]
        n -= (quotitent + 1) * divisor

    answer += numbers[n - 1]

    return answer


if __name__ == '__main__':
    assert solution(5) == '12'
    assert solution(9) == '24'
    assert solution(13) == '111'
    assert solution(44) == '1122'
