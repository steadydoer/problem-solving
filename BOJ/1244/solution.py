# BOJ Coding Test Practice
# 1244: 스위치 켜고 끄기
#
#     https://www.acmicpc.net/problem/1244
#
# ==============================================================================


def toggle_switch(switches, idx):
    if switches[idx] == 0:
        switches[idx] = 1
    else:
        switches[idx] = 0


def solve():
    n = int(input())
    switches = [-1] + [state for state in map(int, input().split())]
    students = int(input())
    for _ in range(students):
        gender, number = list(map(int, input().split()))
        if gender == 1:  # 남학생
            for multi in range(number, n+1, number):
                toggle_switch(switches, multi)
            pass
        elif gender == 2:  # 여학생
            length = min([number - 1, n - number])
            changes = [number]
            for i in range(1, length + 1):
                if switches[number - i] == switches[number + i]:
                    changes.append(number - i)
                    changes.append(number + i)
                else:
                    break
            for idx in changes:
                toggle_switch(switches, idx)
        answer = ''
        for i in range(1, n + 1, 20):
            answer += ' '.join(map(str, switches[i:i+20]))
            answer += '\n'

    return answer


answer = solve()
print(answer[:-1])
