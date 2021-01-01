import sys

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()
temp = float('inf')
result = [0]*3 # 0에 가까운 값들을 저장

for i in range(n - 2):
    # 중복된 값은 건너뛴다
    if i > 0 and liquid[i] == liquid[i - 1]:
        continue

    # 간격을 좁혀가며 sum 계산
    left, right = i+1, n-1

    while left < right:
        total = liquid[i] + liquid[left] + liquid[right]

        if abs(total) < abs(temp):
            result[0], result[1], result[2] = liquid[i], liquid[left], liquid[right]
            temp = total

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            # sum = 0인 경우 정답 처리 후 스킵
            print(liquid[i], liquid[left], liquid[right])
            sys.exit(0)



for i in result:
    print(i, end=' ')
