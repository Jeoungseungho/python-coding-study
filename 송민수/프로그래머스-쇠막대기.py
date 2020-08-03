def solution(arrangement):
    stack=[]
    line=0
    for i in range(len(arrangement)):
        if arrangement[i]=='(':
            stack.append('(')
        elif arrangement[i]==')':
            if arrangement[i-1]=='(':
                line+=(len(stack)-1)
            else:
                line+=1
            stack.pop()
            # print(stack,line)

    return line

print(solution('()(((()())(())()))(())	'))
