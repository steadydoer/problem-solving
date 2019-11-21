# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT 오픈채팅방
#
#     https://programmers.co.kr/learn/courses/30/lessons/42888
#
# total elapsed time: 23:18
# ==============================================================================


def solution(N, stages):
    answer = []
    clear = len(stages)
    fails = {}
    fail_rates = {}
    for stage in stages:
        fails[stage] = fails.get(stage, 0) + 1

    for stage in range(1, N+1):
        user = fails.get(stage, 0)
        if user == 0:
            fail_rates[stage] = 0
        else:
            fail_rate = user / clear
            clear -= user
            fail_rates[stage] = fail_rate
    for stage, fail_rate in sorted(fail_rates.items(), key=lambda item: (item[1], -item[0]), reverse=True):
        answer.append(stage)
    return answer


if __name__ == "__main__":
    inputs = ((5, [2, 1, 2, 6, 2, 4, 3, 3]), (4, [4, 4, 4, 4, 4]))
    outputs = ([3, 4, 2, 1, 5], [4, 1, 2, 3])
    for i in range(len(inputs)):
        N, stages = inputs[i]
        result = outputs[i]
        assert solution(N, stages) == result
