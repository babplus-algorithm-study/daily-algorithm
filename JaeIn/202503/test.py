from copy import deepcopy

T = int(input()) 

for _ in range(T):
    N , R = map(int , input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    # 임시 배열
    arr =  [[0] * N for _ in range(N)]
    
    
    # 각도가 음수일 때
    if R < 0:
        R += 360
    
    # 각도가 - 일 때
    if R == 360 or R == 0:
        for i in board:
            print(*i)
        
    else:
        for _ in range(R // 45):
            mid = N // 2
            
            for i in range(N):
                for j in range(N):
                    # 주 대각선 -> 가운데 열
                    if j == mid:
                        arr[i][j] = board[i][i]
                    # 가운데 열 -> 부 대각선
                    elif i + j == N - 1:
                        arr[i][j] = board[i][mid]
                    # 부 대각선 -> 가운데 행
                    elif i == mid:
                        arr[mid][j] = board[N - 1 - j][j]
                    # 가운데 행 -> 주 대각선
                    elif i == j:
                        arr[i][i] = board[mid][j]
                    # 나머지
                    else:
                        arr[i][j] = board[i][j]
                        
            board = deepcopy(arr)
                        
        for a in arr:
            print(*a)
