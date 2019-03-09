from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = 0
    truck_q = deque(truck_weights)
    bridge_q = deque([0 for x in range(bridge_length)])

    while(truck_q):
        answer += 1
        on_bridge -= bridge_q.popleft()
        if on_bridge + truck_q[0] <= weight:
            truck = truck_q.popleft()
            on_bridge += truck
            bridge_q.append(truck)
        else:
            bridge_q.append(0)

    return answer + bridge_length


if __name__ == "__main__":
    assert solution(2, 10, [7, 4, 5, 6]) == 8
