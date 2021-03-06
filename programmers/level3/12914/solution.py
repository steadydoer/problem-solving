# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/12914
#
# ==============================================================================


def solution(n):
    ways = [0, 1, 2]
    for i in range(3, n+1):
        way = (ways[i-2] + ways[i-1]) % 1234567
        ways.append(way)
    answer = ways[n]
    return answer


if __name__ == "__main__":
    assert solution(4) == 5
    assert solution(3) == 3
