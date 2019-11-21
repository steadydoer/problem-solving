# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/42585
#
# ==============================================================================


def solution(arrangement):
    answer = 0
    stack = [arrangement[0]]
    for idx in range(1, len(arrangement)):
        before_sign = arrangement[idx-1]
        sign = arrangement[idx]
        if sign == '(':
            stack.append(sign)
        else:
            if before_sign == '(':
                answer += len(stack) - 1
            else:
                answer += 1
            stack.pop()
    return answer


def main():
    assert solution('()(((()())(())()))(())') == 17


if __name__ == '__main__':
    main()
