inp = input()

inp_list = []
cnt_list = []
answer = 0
top = ''
for i in inp:
    if i == '(':
        inp_list.append(i)
        cnt_list.append(1)
    elif i == ')':
        if top == '(':
            inp_list.append(i)
            cnt_list.pop()
            for j in range(len(cnt_list)):
                cnt_list[j] += 1
        else:
            inp_list.append(i)
            answer += cnt_list[-1]
            del cnt_list[-1]
    top = inp_list[-1]
    
print(answer)

        
