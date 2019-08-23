# SWEA-2805 농작물 수확하기
# total elapsed time: 52 min


test_case = int(input())
for case in range(1, test_case + 1):
    size = int(input())
    half = size // 2
    start = half
    level = 1
    step = 2
    total = 0
    for _ in range(size):
        row = list(map(int, list(input())))
        if level == size:
            step = -2
        total += sum(row[start:start+level])
        start -= step // 2
        level += step
    print(f'#{case} {total}')
