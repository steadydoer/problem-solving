# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/12953
#
# ==============================================================================


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(arr):
    if len(arr) == 1:
        return arr[0]
    lcm = [i for i in arr]
    for i in range(len(arr) - 1):
        x, y = lcm[i], lcm[i + 1]
        if x < y:
            x, y = y, x
        if x % y == 0:
            lcm[i + 1] = x
            continue
        lcm[i + 1] = (x * y) // get_gcd(x, y)
    answer = lcm[-1]
    return answer


if __name__ == '__main__':
    assert solution([2, 6, 8, 14]) == 168
    assert solution([1, 2, 3]) == 6
