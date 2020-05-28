# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/60057
#
# ==============================================================================


def split_string(s, unit_length):
    return [s[i:i + unit_length] for i in range(0, len(s), unit_length)]


def compress_string(string_units):
    compressed_string = ''
    cnt = 1
    pre_unit = string_units[0]
    for unit in string_units[1:]:
        if pre_unit == unit:
            cnt += 1
            continue
        if cnt == 1:
            compressed = pre_unit
        else:
            compressed = str(cnt) + pre_unit
        compressed_string += compressed
        pre_unit = unit
        cnt = 1
    if cnt == 1:
        compressed = pre_unit
    else:
        compressed = str(cnt) + pre_unit
    compressed_string += compressed
    return compressed_string


def solution(s):
    min_ = len(s)
    for unit_length in range(1, int(len(s) / 2) + 1):
        string_units = split_string(s, unit_length)
        compressed_length = len(compress_string(string_units))
        if min_ > compressed_length:
            min_ = compressed_length
    answer = min_
    return answer


if __name__ == '__main__':
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17
