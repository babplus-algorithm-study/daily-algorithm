```python
import sys
import heapq

input = sys.stdin.readline

N , M = list(map(int , input().split()))
start = int(input())

arr = [[] for _ in range(N + 1)]
dist = [1e9 for _ in range(N + 1)]

for l in range(M):
    a , b, c = list(map(int , input().split()))
    arr[a].append([b , c])


q = []
heapq.heappush(q , [0,start])
dist[start] = 0



while q:
    _w , node = heapq.heappop(q)

    for nxt , weight in arr[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q,  [dist[nxt] , nxt])


for i in range(1 , len(dist)):
    if dist[i] == 1e9:
        print('INF')
    else:
        print(dist[i])
```
