def solution(n):
    nList = list(map(int, str(n)))
    newL = sorted(nList, reverse = True)
    strings = [str(i) for i in newL]
    a_string = "".join(strings)

    return int(a_string)
