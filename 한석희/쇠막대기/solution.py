def solution(arrangement):
    #
    answer = 0
    stack = []
    
    #
    i = 0
    while i < len(arrangement) :
        
        char = arrangement[i]
        
        # "(" -> )
        if char == "(" and arrangement[i+1] == ")" :
            answer += len(stack)
        # "(" -> (
        elif char == "(" and arrangement[i+1] == "(" :
            stack.append("(")
        # ) -> ")"
        elif char == ")" and arrangement[i-1] == ")" :
            stack.pop()
            answer += 1
        # ) -> "("
        elif char == ")" and arrangement[i-1] == "(" :
            i += 1
            continue
            
        #
        i += 1
    
    #
    return answer
