# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/60058
#
# ==============================================================================


def split_bracket(w):
    u = ''
    v = ''
    store = 0
    for i, c in enumerate(w):
        if c == '(':
            store += 1
        else:
            store -= 1
        if store == 0:
            u = w[:i + 1]
            v = w[i + 1:]
            break

    return u, v


def is_correct(s):
    ret = True
    left = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            left -= 1
        if left < 0:
            ret = False
            break

    return ret


def reverse_bracket(bracket):
    ret = '('
    if bracket == '(':
        ret = ')'
    return ret


def convert_bracket(w):
    if w == '':
        return w
    u, v = split_bracket(w)
    if is_correct(u):
        v = convert_bracket(v)
    else:
        v = convert_bracket(v)
        ret = '(' + v + ')' + ''.join([reverse_bracket(c) for c in u[1:-1]])
        return ret
    return u + v


def solution(p):
    if is_correct(p):
        return p
    answer = convert_bracket(p)
    return answer


if __name__ == '__main__':
    assert solution("(()())()") == "(()())()"
    assert solution(")(") == "()"
    assert solution("()))((()") == "()(())()"
