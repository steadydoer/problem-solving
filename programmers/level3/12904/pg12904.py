# Programmers Coding Test Practice
# Level 3 가장 긴 펠린드롬
#
#     https://programmers.co.kr/learn/courses/30/lessons/12904
#
# ==============================================================================


def is_palindrome(s):
    result = True
    if len(s) == 1:
        return result
    for i in range((len(s) + 1) // 2):
        if s[i] != s[-1 - i]:
            result = False
            break
    return result


def get_available_max_length(total_length, mid):
    return min(mid, total_length - 1 - mid) * 2 + 1


def get_palindrome_length(s, mid, even=True):
    palindrome_length = 0
    start = mid
    if even:
        stop = mid + 2
    else:
        stop = mid + 1

    while 0 <= start and stop <= len(s):
        if not is_palindrome(s[start:stop]):
            break
        palindrome_length = stop - start
        start -= 1
        stop += 1
    return palindrome_length


def solution(s):
    answer = 0
    if len(s) % 2 == 0:
        i = (len(s) - 1) // 2
    else:
        i = len(s) // 2
    j = len(s) // 2
    while 0 <= i and j < len(s):
        for mid in [i, j]:
            available_max_length = get_available_max_length(len(s), mid)
            if available_max_length < answer:
                continue
            for even in [False, True]:
                palindrome_length = get_palindrome_length(s, mid, even)
                if answer < palindrome_length:
                    answer = palindrome_length
        i -= 1
        j += 1
    return answer


if __name__ == '__main__':
    assert solution('abcdcba') == 7
    assert solution('abacde') == 3
