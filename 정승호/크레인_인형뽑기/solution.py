def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                
                if (basket[len(basket)-1] == basket[len(basket)-2]) and len(basket) >= 2 :
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
        
    return answer
