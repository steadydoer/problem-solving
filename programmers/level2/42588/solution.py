def solution(heights):
    answer = []
    heights_length = len(heights)
    for i in range(1, heights_length):
        send = heights[-i]
        for j in range(i + 1, heights_length + 1):
            if heights[-j] > send:
                answer.append(heights_length - j + 1)
                break
        else:
            answer.append(0)

    answer.append(0)
    answer.reverse()
    return answer
