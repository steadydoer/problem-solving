# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT 무지의 먹방 라이브
#
#     https://programmers.co.kr/learn/courses/30/lessons/42891
#
# 14:13 정확성 테스트 통과 113:08 효율성 테스트 통과
# total elapsed time: 113:08
# ==============================================================================
from collections import deque


def solution(food_times, k):
    answer = -1

    # 완전탐색
    # food_q = deque(enumerate(food_times))
    # for i in range(k):
    #     if not food_q:
    #         break
    #     food = food_q.popleft()
    #     if food[1] - 1 != 0:
    #         food_q.append((food[0], food[1] - 1))
    # if food_q:
    #     answer = food_q.popleft()[0] + 1
    # else:
    #     answer = -1

    # 효율성 개선 코드
    foods = list(enumerate(food_times, 1))  # (food_number, time)
    foods.sort(key=lambda food: food[1])  # key: time
    previous_time = 0
    foods_index = 0

    while foods_index < len(foods):
        current_time = foods[foods_index][1]
        if previous_time == current_time:
            foods_index += 1
            continue
        else:
            diff_time = current_time - previous_time
            previous_time = current_time
            length = len(foods) - foods_index
            available_loop = k // length
            max_loop = diff_time

            if available_loop >= max_loop:
                k -= diff_time * length
                foods_index += 1
            else:
                # key: food_number
                foods = sorted(foods[foods_index:], key=lambda food: food[0])
                answer = foods[k % length][0]
                break

    return answer


if __name__ == "__main__":
    assert solution([3, 1, 2], 5) == 1
