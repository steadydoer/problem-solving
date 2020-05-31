# Programmers Coding Test Practice
# Level 2 가장 큰 정사각형 찾기
#
#     https://programmers.co.kr/learn/courses/30/lessons/12905
#
# ==============================================================================


def solution(board):
    max_width = 0
    if len(board) == 1:
        for c in range(len(board[0])):
            max_width = max_width | board[0][c]
        return max_width * max_width
    if len(board[0]) == 1:
        for r in range(len(board)):
            max_width = max_width | board[r][0]
        return max_width * max_width
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == 1:
                board[r][c] = min(board[r - 1][c - 1], board[r][c - 1], board[r - 1][c]) + 1
                if max_width < board[r][c]:
                    max_width = board[r][c]
    answer = max_width * max_width
    return answer


if __name__ == '__main__':
    assert solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]) == 9
    assert solution([[0, 0, 1, 1], [1, 1, 1, 1]]) == 4
    assert solution([[0], [1]]) == 1
    assert solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]) == 9
