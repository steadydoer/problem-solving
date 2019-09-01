# BOJ Coding Test Practice
# 2455: 지능형 기차
#
#     https://www.acmicpc.net/problem/2455
#
# ==============================================================================


def solve():
    answer = 0
    station = 4
    train = 0
    for _ in range(station):
        get_out, get_in = list(map(int, input().split()))
        train += get_in - get_out
        if train > answer:
            answer = train
    return answer


answer = solve()
print(answer)
