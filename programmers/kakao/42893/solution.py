# Programmers Coding Test Practice
# 2019 KAKAO BLIND RECRUITMENT 매칭 점수
#
#     https://programmers.co.kr/learn/courses/30/lessons/42893
#
# ==============================================================================
import re


def solution(word, pages):
    answer = 0
    word, pages = word.lower(), [page.lower() for page in pages]
    # 기본 점수, 외부 링크 수, 링크 점수, 매칭 점수
    basic_scores = [0] * len(pages)
    out_links = [[] for _ in range(len(pages))]
    link_scores = [0] * len(pages)
    urls = dict()
    body_pattern = re.compile(r'<.*body.*?>(.*)body.*>', re.S | re.I)
    url_pattern = re.compile(
        r'meta property="og:url" content="(https://.*?)"', re.S | re.I)
    link_pattern = re.compile(r'href="(https://.*?)"', re.S)
    replace_pattern = re.compile('[^a-z]+')
    for idx, page in enumerate(pages):
        url_m = url_pattern.search(page)
        if url_m:
            url = url_m.group(1)
        else:
            url = "-1"
        urls[url] = idx
        body = body_pattern.search(page).group(1)
        basic_scores[idx] = replace_pattern.sub(' ', body).split().count(word)
        out_links[idx] = link_pattern.findall(page)

    for idx in range(len(basic_scores)):
        out_link_size = len(out_links[idx])
        if out_link_size:
            link_scores[idx] = basic_scores[idx] / out_link_size
    matching_scores = [s for s in basic_scores]
    for idx, out_link in enumerate(out_links):
        for link in out_link:
            if link in urls:
                matching_scores[urls[link]] += link_scores[idx]

    answer = max(enumerate(matching_scores),
                 key=lambda pair: (pair[1], -pair[0]))[0]
    return answer


if __name__ == '__main__':
    assert solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                             "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]) == 1
