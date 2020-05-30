# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT [3차] 방금그곡
#
#     https://programmers.co.kr/learn/courses/30/lessons/17683
#
# ==============================================================================
from datetime import datetime


def tokenizer(melody):
    token = []
    for c in melody:
        if c == '#':
            token.append(token.pop() + c)
        else:
            token.append(c)
    return token


def get_play_time(begin, end):
    begin_time = datetime.strptime(begin, '%H:%M')
    end_time = datetime.strptime(end, '%H:%M')
    minutes = int((end_time - begin_time).total_seconds() / 60)
    return minutes


def make_full_melodies(musicinfos):
    full_melodies = {}
    for musicinfo in musicinfos:
        begin, end, title, melody = musicinfo.split(',')
        melody = tokenizer(melody)
        play_time = get_play_time(begin, end)
        full_melody = melody * (play_time // len(melody)) + melody[:play_time % len(melody)]
        full_melodies[title] = full_melody
    return full_melodies


def search_melody(m, full_melodies):
    match_melodies = []
    match_title = '(None)'
    m = tokenizer(m)
    for title, melody in full_melodies.items():
        if len(m) > len(melody):
            continue
        for i in range(0, len(melody) - len(m) + 1):
            if m == melody[i:i + len(m)]:
                match_title = title
                match_melodies.append({'title': title, 'play_time': len(melody)})
                break

    if match_melodies:
        match_melodies.sort(key=lambda info: info['play_time'], reverse=True)
        match_title = match_melodies[0]['title']
    return match_title


def solution(m, musicinfos):
    full_melodies = make_full_melodies(musicinfos)
    answer = search_melody(m, full_melodies)
    return answer


if __name__ == '__main__':
    assert solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']) == 'HELLO'
    assert solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']) == 'FOO'
    assert solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']) == 'WORLD'
