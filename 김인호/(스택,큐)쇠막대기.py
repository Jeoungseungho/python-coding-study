# cutN : 잘린 막대기 수
# num : 잘리지 않은 원래 막대기 수

def solution(arrangment):
    arr = arrangment.replace("()", "L")
    cutN, num = 0, 0

    for i in arr:
        if i == "(":
            cutN += 1
            num += 1
        elif i == ")":
            num -= 1
        else:
            cutN += num
    print(cutN)
    return cutN

s = input()
solution(s)
