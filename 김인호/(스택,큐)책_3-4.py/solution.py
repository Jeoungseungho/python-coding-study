MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"

def move(N, start, to):
    temp = dic[start].pop()
    dic[to].append(temp)
    print(MSG_FORMAT.format(N, start, to))


def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N - 1, start, via, to)
        move(N, start, to)
        hanoi(N - 1, via, to, start)

N = int(input())
dic = {}
dic["A"] = [i for i in range(N, 0, -1)]
dic["B"], dic["C"] = [], []

hanoi(N, "A", "C", "B")
print("마지막 탑 :", dic["C"])
