# BOJ Coding Test Practice
# 17136: 색종이 붙이기
#
#     https://www.acmicpc.net/problem/17136
#
# ==============================================================================


def check_square(board, y, x, size):
    if y + size > 10 or x + size > 10:
        return False
    for r in range(y, y+size):
        for c in range(x, x+size):
            if not board[r][c]:
                return False

    return True


def fill_square(board, y, x, size, state):
    for r in range(y, y+size):
        for c in range(x, x+size):
            board[r][c] = state


def solve():
    answer = 0
    n = 10
    board = [[number for number in list(
        map(int, input().split()))] for _ in range(n)]
    papers = [0 for _ in range(6)]
    ones = 0
    for b in board:
        ones += b.count(1)
    if not ones:
        return answer
    min_ = [100]

    def dfs(y, x, cnt, filled_ones, total_ones, min_):
        nonlocal board
        nonlocal papers
        if min_[0] <= cnt:
            return
        if filled_ones == total_ones:
            min_[0] = min([min_[0], cnt])
        if x == 10:
            y += 1
            x = 0
        if y == 10:
            return

        stop = False
        for r in range(y, 10):
            for c in range(10):
                if board[r][c]:
                    stop = True
                    break
            if stop:
                break
        if not stop:
            return

        for color_size in range(5, 0, -1):
            if check_square(board, r, c, color_size) and papers[color_size] < 5:
                papers[color_size] += 1
                fill_square(board, r, c, color_size, 0)
                dfs(r, c+1, cnt+1, filled_ones +
                    color_size * color_size, total_ones, min_)
                papers[color_size] -= 1
                fill_square(board, r, c, color_size, 1)

    dfs(0, 0, 0, 0, ones, min_)
    if min_[0] == 100:
        answer = -1
    else:
        answer = min_[0]
    return answer


answer = solve()
print(answer)
