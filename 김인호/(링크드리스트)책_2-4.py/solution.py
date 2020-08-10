class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# 링크드 리스트 value 와 x 값을 입력 받는다.
arr = list(map(int,input().split()))
x_value = int(input())

# 링크드리스트 생성
h = None
for i in range(len(arr)-1,-1,-1):
    Node(arr[i],h)
    h = Node(arr[i],h)

temp = h
print("====linked list====")
while h != None:
    if h.next != None:
        print(h.val, end = ' ')
    else:
        print(h.val)
    h = h.next
    
# x 노드만 빼기
h = temp
while True:
    if h.next == None:
        break
    if h.next.val == x_value:
        isFind = True
        nh = h.next
        h.next = h.next.next
        nh.next = None
        break
    h = h.next

# x 노드 기준으로 작으면 왼쪽 크거나 같으면 오른쪽으로 노드들을 붙이기
nt = nh
while temp != None:
    next_node = temp.next
    if temp.val < x_value:
        temp.next = nh
        nh = temp
    else:
        nt.next = temp
        nt = temp
        nt.next = None
    temp = next_node

# 새로운 링크드 리스트 출력.
print("====New linked list====")
while nh != None:
    if nh.next != None:
        print(nh.val, end = ' ')
    else:
        print(nh.val)
    nh = nh.next

# 테스트 코드
# 4 3 2 6
# 3


# 4 3 1 5 6 7 8 9
# 6


# 1 1 1 3 3 3 2 2 2 4 4
# 3

# 3 3 3 3 1
# 1