# Programmers Coding Test Practice
# Level 3
#
#     https://programmers.co.kr/learn/courses/30/lessons/42895
#
# ==============================================================================


def solution(N, number):
    case_sets = [{N}]
    for i in range(2, 9):
        case_set = {int(str(N) * i)}
        for x_idx in range(i//2):
            for x in case_sets[x_idx]:
                for y in case_sets[i - x_idx - 2]:
                    case_set.add(x + y)
                    case_set.add(x - y)
                    case_set.add(y - x)
                    case_set.add(x * y)
                    if x != 0:
                        case_set.add(y // x)
                    if y != 0:
                        case_set.add(x // y)
        if number in case_set:
            return i
        case_sets.append(case_set)
    return -1


if __name__ == '__main__':
    assert solution(5, 12) == 4
    assert solution(2, 11) == 3
