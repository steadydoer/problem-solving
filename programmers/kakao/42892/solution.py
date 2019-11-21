# Programmers Coding Test Practice
# 2019 KAKAO BLIND RECRUITMENT 길 찾기 게임
#
#     https://programmers.co.kr/learn/courses/30/lessons/42892
#
# ==============================================================================
from collections import deque


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.loc = None

    def __str__(self):
        return f'value:{self.data}'


def connect_node(upper, lower):
    upper_x, _ = upper.loc
    lower_x, _ = lower.loc
    if lower_x < upper_x:
        if upper.left is None:
            upper.left = lower
        else:
            connect_node(upper.left, lower)
    else:
        if upper.right is None:
            upper.right = lower
        else:
            connect_node(upper.right, lower)


def preorder(node, result):
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


def solution(nodeinfo):
    answer = []
    enum_nodeinfo = list(enumerate(nodeinfo, 1))  # number, location
    enum_nodeinfo.sort(key=lambda info: (-info[1][1], info[1][0]))
    root = Node(enum_nodeinfo[0][0])
    root.loc = enum_nodeinfo[0][1]
    node_q = deque(enum_nodeinfo[1:])
    while node_q:
        value, loc = node_q.popleft()
        child = Node(value)
        child.loc = loc
        connect_node(root, child)
    pre_node = []
    post_node = []
    preorder(root, pre_node)
    postorder(root, post_node)
    answer.append(pre_node)
    answer.append(post_node)

    return answer


if __name__ == "__main__":
    assert solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [
                    7, 2], [2, 2]]) == [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
