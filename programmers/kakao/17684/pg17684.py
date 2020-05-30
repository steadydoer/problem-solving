# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [3차] 압축
#
#     https://programmers.co.kr/learn/courses/30/lessons/17684
#
# ==============================================================================
from string import ascii_uppercase


def solution(msg):
    answer = []
    lzw = {v: i for i, v in enumerate(ascii_uppercase, 1)}
    begin = 0
    while begin < len(msg):
        contain = True
        length = 1
        while contain and begin+length <= len(msg):
            contain = False
            wc = msg[begin:begin + length]
            if wc in lzw:
                contain = True
                length += 1
                continue
            lzw[wc] = len(lzw) + 1
        w = msg[begin:begin + length - 1]
        begin += length - 1
        if w in lzw:
            answer.append(lzw[w])

    return answer


if __name__ == '__main__':
    assert solution('KAKAO') == [11, 1, 27, 15]
    assert solution('TOBEORNOTTOBEORTOBEORNOT') == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    assert solution('ABABABABABABABAB') == [1, 2, 27, 29, 28, 31, 30]
