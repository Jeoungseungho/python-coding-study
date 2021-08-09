def get_score(avg):
    if avg >= 90: return 'A'
    elif 80 <= avg < 90: return 'B'
    elif 70 <= avg < 80: return 'C'
    elif 50 <= avg < 70: return 'D'
    else : return 'F'

    
def solution(scores):
    answer = ''
    for j in range(len(scores[0])):
        score_sum = 0
        my_score_list = []
        
        for i in range(len(scores)):
            score_sum += scores[i][j]
            my_score_list.append(scores[i][j])
            if i == j:
                my_score = scores[i][j]
                
        my_score_list.sort()    
        
        if (my_score_list[0] != my_score_list[1]) and (my_score_list[0] == my_score) :
            score_sum -= my_score
            answer += get_score(score_sum/((len(scores[0]))-1))
        elif (my_score_list[-1] != my_score_list[-2]) and (my_score_list[-1] == my_score):
            score_sum -= my_score
            answer += get_score(score_sum/(len(scores[0])-1))
        else:
            answer += get_score(score_sum/len(scores[0]))
             

            
    return answer
