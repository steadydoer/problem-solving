# Programmers Coding Test Practice
# Level 5
#
#     https://programmers.co.kr/learn/courses/30/lessons/17680
#
# ==============================================================================


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    cities = map(str.lower, cities)
    cache = []
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if cacheSize <= len(cache):
                cache = cache[1:]
            cache.append(city)
    return answer


if __name__ == "__main__":
    assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
                        "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA]"]) == 50
