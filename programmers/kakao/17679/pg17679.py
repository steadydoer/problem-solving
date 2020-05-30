# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록
#
#     https://programmers.co.kr/learn/courses/30/lessons/17679
#
# ==============================================================================


def check_square(m, n, board, r, c):
    checked_block = set()
    if r < 0 or m - 1 <= r or c < 0 or n - 1 <= c:
        return checked_block
    if board[r][c] == ' ':
        return checked_block
    if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1]:
        for i in range(2):
            for j in range(2):
                checked_block.add((r + i, c + j))
    return checked_block


def delete_block(board, checked_block):
    for r, c in checked_block:
        board[r][c] = ' '


def fill_board(m, n, board):
    for c in range(n):
        idx = m
        for r in range(m - 1, -1, -1):
            if board[r][c] == ' ':
                continue
            idx -= 1
            if idx == r:
                continue
            board[idx][c], board[r][c] = board[r][c], board[idx][c]


def check_board(m, n, board):
    deleted_cnt = 0
    is_deleted = True
    while is_deleted:
        is_deleted = False
        checked_block = set()
        for r in range(m):
            for c in range(n):
                checked_block |= check_square(m, n, board, r, c)
        if not checked_block:
            continue
        deleted_cnt += len(checked_block)
        delete_block(board, checked_block)
        fill_board(m, n, board)
        is_deleted = True

    return deleted_cnt


def update_board(m, n, board):
    board = [list(row) for row in board]
    deleted_block = check_board(m, n, board)
    return deleted_block


def solution(m, n, board):
    answer = update_board(m, n, board)
    return answer


if __name__ == '__main__':
    assert solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']) == 14
    assert solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']) == 15
