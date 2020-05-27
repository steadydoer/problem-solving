# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/62048
#
# ==============================================================================


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def solution(w, h):
    gcd_wh = gcd(w, h)
    unit = int(w / gcd_wh + h / gcd_wh - 1)
    answer = w * h - unit * gcd_wh
    return answer


if __name__ == '__main__':
    assert solution(8, 12) == 80
