# Programmers Coding Test Practice
# Level 3 거스름돈
#
#     https://programmers.co.kr/learn/courses/30/lessons/12907
#
# ==============================================================================


def solution(n, money):
    money.sort()
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(money[0], n + 1, money[0]):
        dp[i] = 1
    for money_unit in money[1:]:
        for i in range(money_unit, n + 1):
            dp[i] += dp[i - money_unit] % 1000000007
    answer = dp[n]
    return answer


if __name__ == '__main__':
    assert solution(5, [1, 2, 5]) == 4
