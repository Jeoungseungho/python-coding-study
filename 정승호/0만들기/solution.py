test_case = int(input())
answer = []

def dfs(arr, index, susik1, susik2):
    if index == (len(arr)-1):
        susik1 += str(arr[index])
        susik2 += str(arr[index])
        n = int(eval(susik1))
        if n == 0:
            answer.append(susik2)
    else:
        dfs(arr, index+1, susik1 + str(arr[index]),susik2 + str(arr[index])+ " " )
        dfs(arr, index+1, susik1 + str(arr[index])+'+',susik2 + str(arr[index])+'+')
        dfs(arr, index+1, susik1 + str(arr[index])+'-', susik2 + str(arr[index])+'-')

for _ in range(test_case):
    n = int(input())
    arr = [i for i in range(1, n+1)]
    dfs(arr,0,"","")
    for i in answer:
        print(i)
    print()
    answer.clear()
