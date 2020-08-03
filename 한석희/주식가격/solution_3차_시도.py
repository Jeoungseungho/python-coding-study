def solution(prices):

    # price의 사이즈 재기
    size = len(prices)
    # price의 길이에 맞게 answer만들기
    answer = [0] * size
    # 스택 리스트 만들기
    stack = []
    
    # 프라이스 이터레이션 시작
    for i in range(size) :
    # 스택이 비어있지 않고, 새로들어온 주가에 비해, 스택 맨 위의 주가가 "높다면"
        while (stack) and ( stack[ -1 ] > prices[ i ] ) :
            poppedIndex = stack.pop()
            answer[ poppedIndex ] = i - poppedIndex
    # 새로운 요소(인덱스)를 스택에 넣는다.
        stack.append( i )
    
    # 스택에 남은 거 떨기
    while stack :
    # 스택 하나하나 마다
        poppedIndex = stack.pop()
    #   프라이스의 사이즈 - 1에서 그 값 뺀 값을
        answer[ poppedIndex ] = ( ( size - 1 ) - poppedIndex )
                        
    return answer
