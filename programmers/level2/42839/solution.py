# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/42839
#
# ==============================================================================
import copy
from math import sqrt


def swap(list_, x, y):
    list_[x], list_[y] = list_[y], list_[x]
    return


def get_permutation(numbers, depth, num_len, goal, permutation):
    if depth == goal:
        number = ''.join(numbers)
        permutation.append(number)
        return
    for i in range(depth, num_len):
        swap(numbers, i, depth)
        get_permutation(numbers, depth + 1, num_len, goal, permutation)
        swap(numbers, i, depth)
    return


def get_prime_numbers(last_number):
    prime_numbers = [2]
    for number in range(3, last_number+1):
        limit = int(sqrt(number) + 2)
        for prime_number in prime_numbers:
            if prime_number > limit:
                prime_numbers.append(number)
                break
            if number % prime_number == 0:
                break
        else:
            prime_numbers.append(number)

    return prime_numbers


def get_candidates(permutation):
    candidates = set()
    for number in permutation:
        for i in range(len(number)):
            candidates.add(int(number[i:]))
    candidates = sorted(list(candidates))
    return candidates


def solution(numbers):
    answer = 0
    permutation = []
    get_permutation(list(numbers), 0, len(numbers), len(numbers),  permutation)
    candidates = get_candidates(permutation)
    max_ = candidates[-1]
    prime_numbers = get_prime_numbers(max_)
    for candidate in candidates:
        if candidate in prime_numbers:
            answer += 1
    return answer


if __name__ == '__main__':
    numbers1 = '17'
    numbers2 = '011'
    answer1 = solution(numbers1)
    answer2 = solution(numbers2)
    assert answer1 == 3, f'기댓값 3과 결과값 {answer1}가 다릅니다.'
    assert answer2 == 2, f'기댓값 2와 결과값 {answer2}가 다릅니다.'
