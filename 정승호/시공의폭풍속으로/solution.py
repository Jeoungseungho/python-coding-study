teamInput = list(map(int, input().split(" ")))
myChoice = list(map(int,input().split(" "))) 

hero = [0]*100
answer = 0
for i in teamInput:
	hero[i] += 1
	
for j in myChoice:
	if hero[j] == 0:
		answer +=1
		
print(answer)

#goorm 
