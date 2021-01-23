def solution(s):
    P_num ,Y_num = 0, 0 
    s = s.lower()
    
    for i in s:
        if i == 'p':
            P_num +=1
        elif i == 'y' : 
            Y_num +=1
            
    if P_num == Y_num:
        return True
    
    return False
