def solution(s):

    length = len(s)
    slic = len(s) // 2

    for k in range(1, slic + 1):
        is_duplicate = False
        temp = ""
        idx = 0
        cnt = 1

        while idx + k < len(s):
            if s[idx : idx + k] == s[idx + k : idx + k + k]:
                is_duplicate = True
                cnt += 1
            else:
                if is_duplicate:
                    temp = temp + str(cnt) + s[idx : idx + k]
                    cnt = 1
                    is_duplicate = False
                else:
                    temp += s[idx : idx + k]

            idx += k

        #  마지막 부분
        if is_duplicate:
            temp = temp + str(cnt) + s[idx : idx + k]
        else:
            temp += s[idx : idx + k]

        length = min(length, len(temp))

    return length
