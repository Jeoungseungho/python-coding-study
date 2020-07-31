import numpy as np

def solution(prices):
    
    # 1. ind, val stack (array)
    indexValueStack = []
    # 2. lastedTimeStack (array)
    lastedTimeStack = np.array( [] )
    # 3. 결과 튜플
    resultTuplesArray = []
    
    # 프라이스 이터레이션
    for index, price in enumerate(prices) :
        
        # 처음이면 그냥 넣기
        if not indexValueStack :
            indexValueStack.append( [index, price] )
            lastedTimeStack = np.append(lastedTimeStack, 0)
            continue
        
        # 요소가 있었으면 탑 요소 피크
        topElement = indexValueStack[-1][1]
            # 새로운 요소 < 탑 요소
        if topElement > price :
            
            while topElement > price :
                
                # pop two stack => merge and append to result
                topElement = indexValueStack.pop()
                topLastedTime = lastedTimeStack[-1] + 1 # 가설 : 넘파이 덧셈이 O(1)이 아닌 경우
                lastedTimeStack = lastedTimeStack[:-1]
                
                # append to result
                resultTuplesArray.append( ( topElement[0], topElement[1], topLastedTime ) )
                
                # if it's already empty - don't need to go out
                if not indexValueStack :
                    break
                    
                # for next element try !!
                topElement = indexValueStack[-1][1]
            
            # 이후 남아있는 lastedTimestack numpy + 1 해준다.
            lastedTimeStack = np.add( lastedTimeStack, np.ones( len(lastedTimeStack) ) )
            
            # 새로운 요소의 (인덱스, 값)을 1에 푸쉬, 2에 0 푸쉬 해준다.
            indexValueStack.append( [index, price] )
            lastedTimeStack = np.append(lastedTimeStack, 0)
            
        # 새로운 요소가 탑 요소보다 크거나 같을 때
        else :
            # 2에 +1을 해준후
            lastedTimeStack = np.add( lastedTimeStack, np.ones( len(lastedTimeStack) ) )
            # 새로운 요소 (인덱스, 값)을 1에 푸쉬 새로운 요소를 위한 0 푸쉬
            indexValueStack.append( [index, price] )
            lastedTimeStack = np.append(lastedTimeStack, 0)
                
    # 이터레이션 끝
    
        # 스택에 남아있는 것을 튜플로 합쳐서 결과 튜플로 가져오기 !!
    for i in range( len(indexValueStack) ):
        resultTuplesArray.append( ( indexValueStack[i][0], indexValueStack[i][1], lastedTimeStack[i] ) )
        # 결과를 인덱스 기준으로 오름차순 정렬
    resultTuplesArray = sorted( resultTuplesArray, key=lambda x: x[0], reverse=False)
        # 떨어지지 않은 지속 시간만 남긴다.
    answer = [ int(i[2]) for i in resultTuplesArray ]
    
    return answer
