def solution(dartResult):
    answer = [0]
    for s in dartResult:
        if s== 'S':
            answer[-1] **= 1
            answer.append(0)
        elif s=='D':
            answer[-1] **= 2
            answer.append(0)
        elif s=='T':
            answer[-1]**=3
            answer.append(0)
        elif s == '*':
            answer[-2]*=2
            if len(answer) > 2:
                answer[-3]*=2
        elif s == '#':
            answer[-2] *= -1
        else:
            answer[-1] = answer[-1]*10 + int(s)
            
    return sum(answer)
