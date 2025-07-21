```python
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = float("-inf")
min_num = float("inf")

def dfs(n, cur_sum):

    global max_num, min_num

    if n == N - 1:
        max_num = max(max_num, cur_sum)
        min_num = min(min_num, cur_sum)
        return


    if op[0] > 0: # 덧셈
        op[0] -= 1
        dfs(n + 1 , cur_sum + numbers[n + 1])
        op[0] += 1
    if op[1] > 0: # 뺄셈
        op[1] -= 1
        dfs(n + 1 , cur_sum - numbers[n + 1])
        op[1] += 1
    if op[2] > 0: # 곱하기
        op[2] -= 1
        dfs(n + 1 , cur_sum * numbers[n + 1])
        op[2] += 1
    if op[3] > 0: # 나누기
        op[3] -= 1
        dfs(n + 1 , int(cur_sum / numbers[n + 1]))
        op[3] += 1


dfs(0 , numbers[0])
print(max_num)
print(min_num)

```
