# Programmers Coding Test Practice
# Level 2
#
#     https://programmers.co.kr/learn/courses/30/lessons/42578
#
# ==============================================================================


def solution(clothes):
    answer = 1
    classified_clothes = {}
    for cloth, cloth_type in clothes:
        value = classified_clothes.get(cloth_type, [])
        value.append(cloth)
        classified_clothes[cloth_type] = value
    for cloth_type, cloth in classified_clothes.items():
        answer *= len(cloth) + 1
    answer -= 1
    return answer


if __name__ == '__main__':
    assert solution([['yellow_hat', 'headgear'],
                     ['blue_sunglasses', 'eyewear'],
                     ['green_turban', 'headgear']]) == 5
    assert solution([['crow_mask', 'face'],
                     ['blue_sunglasses', 'face'],
                     ['smoky_makeup', 'face']]) == 3
