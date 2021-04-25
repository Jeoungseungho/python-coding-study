N = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()
M = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    start = 0
    end = N-1
    target = i
    answer = 0
    while(start <= end):
        mid = (start+end)//2
        if arr_n[mid]==target:
            answer = 1
            break
        elif target < arr_n[mid]:
            end = mid-1
        else:
            start = mid+1
    print(answer)




