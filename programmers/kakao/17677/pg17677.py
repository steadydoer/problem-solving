# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링
#
#     https://programmers.co.kr/learn/courses/30/lessons/17677
#
# ==============================================================================
from string import ascii_uppercase
from copy import deepcopy


def get_multiple_set(string):
    string = string.upper()
    multiple_set = []

    for i in range(len(string) - 1):
        if string[i] in ascii_uppercase and string[i + 1] in ascii_uppercase:
            multiple_set.append(string[i] + string[i + 1])

    return multiple_set


def get_intersection(multiset1, multiset2):
    intersection = []
    multiset2 = deepcopy(multiset2)
    for element in multiset1:
        if element in multiset2:
            intersection.append(element)
            multiset2.remove(element)

    return intersection


def solution(str1, str2):
    multiplier = 65536
    multiset1 = get_multiple_set(str1)
    multiset2 = get_multiple_set(str2)
    intersection = get_intersection(multiset1, multiset2)

    divider = len(multiset1) + len(multiset2) - len(intersection)

    if divider == 0:
        return multiplier
    answer = int(multiplier * len(intersection) / (len(multiset1) + len(multiset2) - len(intersection)))
    return answer


if __name__ == '__main__':
    assert solution('FRANCE', 'french') == 16384
    assert solution('handshake', 'shake hands') == 65536
    assert solution('aa1+aa2', 'AAAA12') == 43690
    assert solution('E=M*C^2', 'e=m*c^2') == 65536
