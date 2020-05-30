# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬
#
#     https://programmers.co.kr/learn/courses/30/lessons/17686
#
# ==============================================================================


def compare(file_name):
    first = False
    num_start = 0
    num_stop = 0
    for i, c in enumerate(file_name):
        if c.isdigit():
            if not first:
                first = True
                num_start = i
        else:
            if first:
                num_stop = i
                break
    if num_stop == 0:
        num_stop = len(file_name)
    head, number = file_name[:num_start], file_name[num_start:num_stop]

    return head.lower(),  number.zfill(5)


def solution(files):
    answer = sorted(files, key=compare)
    return answer


if __name__ == '__main__':
    assert solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']) ==  ['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png']
    assert solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']) == ['A-10 Thunderbolt II', 'B-50 Superfortress', 'F-5 Freedom Fighter', 'F-14 Tomcat']