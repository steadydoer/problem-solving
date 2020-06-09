# Programmers Coding Test Practice
# Level 3 예산
#
#     https://programmers.co.kr/learn/courses/30/lessons/43237
#
# ==============================================================================


def solution(budgets, M):
    budgets.sort()
    totals = [budgets[0]]
    estimated_total = [budgets[0] * len(budgets)]
    if estimated_total[-1] > M:
        return M // len(budgets)
    for i, budget in enumerate(budgets[1:], 1):
        estimated_total.append(totals[-1] + budget * (len(budgets) - i))
        if estimated_total[-1] > M:
            break
        totals.append(totals[-1] + budget)
    else:
        return budgets[-1]

    answer = (M - estimated_total[i - 1]) // (len(budgets) - i) + budgets[i - 1]
    return answer


if __name__ == '__main__':
    assert solution([120, 110, 140, 150], 485) == 127
