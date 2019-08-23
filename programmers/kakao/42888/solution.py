# Programmers Coding Test Practice
# 2018 KAKAO BLIND RECRUITMENT 오픈채팅방
#
#     https://programmers.co.kr/learn/courses/30/lessons/42888
#
# total elapsed time: 24:41
# ==============================================================================


def solution(record):
    answer = []
    original = []
    nicknames = dict()
    default_messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for r in record:
        informations = r.split()
        if len(informations) == 3:
            command, uid, nickname = informations
            nicknames[uid] = nickname
        else:
            command, uid = informations

        if command in default_messages.keys():
            original.append((uid, default_messages[command]))

    answer = [nicknames[uid] + default_message
              for uid, default_message in original]
    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
              "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    assert solution(record) == result
