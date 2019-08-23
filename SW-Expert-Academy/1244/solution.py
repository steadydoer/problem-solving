# SWEA-1244 최대상금
# total elapsed time: 136 min


def do_exchange(number, begin, exchange):
    if len(number) - begin == 2:
        if number[-2] in number[:-2]:
            pass
        else:
            number[-2], number[-1] = number[-1], number[-2]
        return begin, exchange - 1
    rest = number[begin:]
    end = 0
    max_ = max(rest)
    if rest[0] == max_:
        return begin + 1, exchange
    count_ = rest.count(max_)
    for i in range(len(rest)):
        if rest[i] > max_:
            end = i
            break
    else:
        end = len(rest)
    availabe_exchange = min([count_, end, exchange])
    if availabe_exchange == 0:
        return begin + 1, exchange
    else:
        part = rest[:availabe_exchange]
        part.sort()
        max_indicies = []
        for i in range(begin, len(number)):
            if number[i] == max_:
                max_indicies.append(i)
        for i in range(availabe_exchange):
            number[i+begin] = max_
            number[max_indicies[-(i+1)]] = part[i]
        return begin + availabe_exchange, exchange - availabe_exchange


test_case = int(input())
for case in range(1, test_case + 1):
    number, exchange = list(map(int, input().split(" ")))
    number = list(map(int, list(str(number))))
    begin = 0
    while exchange != 0:
        begin, exchange = do_exchange(number, begin, exchange)
    answer = ''.join(map(str, number))
    print(f'#{case} {answer}')
