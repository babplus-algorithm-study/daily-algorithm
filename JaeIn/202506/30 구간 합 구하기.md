```python
import sys
input = sys.stdin.readline
from math import ceil, log

N, M, K = map(int , input().split())
l = []
h = ceil(log(N,2))
tree = [0] * 2**(h + 1)


def tree_init(start , end , index):
    if start == end:
        tree[index] = l[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = tree_init(start, mid, index*2) + tree_init(mid + 1 , end , index*2+1)
    return tree[index]


def tree_search(start, end , left , right , index):
    if start > right or end < left:
        return 0

    if start >= left and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return tree_search(start, mid , left ,right, index*2) + tree_search(mid + 1, end, left, right, index*2+1)


def tree_update(start, end , update_index , diff , index):
    if start > update_index or end < update_index:
        return

    tree[index] += diff

    if start == end:
        return

    mid = (start + end) // 2
    tree_update(start, mid, update_index, diff, index*2)
    tree_update(mid + 1, end, update_index, diff, index*2+1)


for _ in range(N):
    l.append(int(input()))



tree_init(0, N-1, 1)

for _ in range(M + K):
    a, b, c = map(int , input().split())

    if a == 1:
        diff = c - l[b-1]
        l[b-1] = c
        tree_update(0, N-1 , b-1, diff, 1)


    elif a == 2:
        print(tree_search(0, N-1, b-1 , c-1, 1))
```
