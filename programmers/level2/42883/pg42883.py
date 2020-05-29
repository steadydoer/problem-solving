# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/42883
#
# ==============================================================================


def select_number(numbers, begin_idx, required_number_length, selected_number):
    if len(numbers) - begin_idx == required_number_length:
        selected_number.extend(numbers[begin_idx:])
        return begin_idx, -1
    max_ = 0
    for i in range(begin_idx, len(numbers) - required_number_length):
        if max_ < numbers[i]:
            max_ = numbers[i]
            begin_idx = i + 1
        if max_ == 9:
            break

    selected_number.append(max_)
    return begin_idx, required_number_length - 1


def solution(number, k):
    numbers = list(map(int, number))
    required_number_length = len(numbers) - k - 1
    selected_number = []
    begin_idx = 0

    while required_number_length != -1:
        begin_idx, required_number_length = select_number(numbers, begin_idx, required_number_length, selected_number)

    answer = ''.join(map(str, selected_number))
    return answer


if __name__ == '__main__':
    assert solution('1924', 2) == '94'
    assert solution('1231234', 3) == '3234'
    assert solution('4177252841', 4) == '775841'
