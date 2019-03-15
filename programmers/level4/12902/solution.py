# Programmers Coding Test Practice
# Level 4
#
#     https://programmers.co.kr/learn/courses/30/lessons/12902
#
# ==============================================================================


def solution(n):
    ways = [1, 0, 3]
    for i in range(3, n+1):
        way = 0
        if i % 2 == 0:
            way = ways[i-2] * 3
            for j in range(4, i+1, 2):
                way += ways[i-j] * 2
        way %= 1000000007
        ways.append(way)
    answer = ways[n]
    return answer


if __name__ == "__main__":
    assert solution(4) == 11
