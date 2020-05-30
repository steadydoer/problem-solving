# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임
#
#     https://programmers.co.kr/learn/courses/30/lessons/17687
#
# ==============================================================================


def change_base(num, base):
    base_characters = [str(i) for i in range(10)]
    base_characters += list('ABCDEF')
    notation = ''
    if num == 0:
        return '0'
    while num != 0:
        notation = str(base_characters[num % base]) + notation
        num = num // base
    return notation


def solution(n, t, m, p):
    answer = ''
    num = 0
    order = 1
    p %= m
    while len(answer) < t:
        notation = change_base(num, n)
        for c in notation:
            if order % m == p:
                answer += c
            order += 1
        num += 1
    answer = answer[:t]
    return answer


if __name__ == '__main__':
    assert solution(2, 4, 2, 1) == '0111'
    assert solution(16, 16, 2, 1) == '02468ACE11111111'
    assert solution(16, 16, 2, 2) == '13579BDF01234567'
