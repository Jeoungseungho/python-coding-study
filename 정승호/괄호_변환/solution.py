def balanceCheck(s):
    temp = 0
    for i in s:
        if i == '(': temp +=1
        else : temp -=1 
            
    if temp == 0 : return True
    else : return False
    
def checkCorrect(s):
    stack=[]
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True


def solution(p):
    answer = ''
    u = ''
    v = ''
    if len(p) == 0 or checkCorrect(p):
        return p
    for i in range(2,len(p)+1,2):
        if balanceCheck(p[0:i]):
            u=p[0:i]
            v=p[i:len(p)]
            break
    if checkCorrect(u):
        answer+=u+solution(v)
    else :
        answer+='('+solution(v)+')'
        for c in u[1:-1]:
            if c=='(': 
                answer+=')'
            else : 
                answer+='('
    return answer
