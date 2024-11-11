import sys
input = sys.stdin.readline

n, k  = map(int , input().split())
bag = [list(map(int , input().split())) for _ in range(n)]

answer = 0
def dfs(idx , weight , value):
    global answer
    if weight > k:
        return
    
    if idx == n:
        answer = max(answer , value)
        return
    
    # 가방을 선택한 경우
    dfs(idx + 1 , weight + bag[idx][0] , value + bag[idx][1])
    
    # 가방을 선택하지 않은 경우
    dfs(idx + 1 , weight , value)

dfs(0 , 0 , 0)
print(answer)
