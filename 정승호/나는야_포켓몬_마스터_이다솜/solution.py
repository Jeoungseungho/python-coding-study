import sys

input = sys.stdin.readline

N, M = map(int, input().split())
book = dict()
index_list = []
for i in range(1, N+1):
    poketmon = input().rstrip()
    book[poketmon] = i
    index_list.append(poketmon)

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(index_list[int(query)-1])
    else:
        print(book[query])



