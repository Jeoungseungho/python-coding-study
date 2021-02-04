def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list=list(skill)
        for i in skills:
            if i in skill:
                if i != skill_list.pop(0): #skill에 포함되는 값이 skill의 첫번째 요소와 일치하는지
                    break
        else:		#for - else 문은 break에 걸리지 않고 끝까지 시행됬을때 작동한다
            answer+=1
    return answer
