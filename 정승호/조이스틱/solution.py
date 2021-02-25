def solution(name):
    answer = 0
    name=list(name)
    index=0
    while(True):
        right=1
        left=1
        if name[index] != 'A': 
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer
