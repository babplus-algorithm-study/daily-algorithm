```python
def solution(m, n, board):
    cnt = 0
    while True:
        cnt_lst = []
        for j in range(m-1):
            for i in range(n-1):
                if board[j][i] == board[j + 1][i] == board[j][i + 1] == board[j + 1][i + 1] != '0':
                    cnt_lst.append([j, i])
                    cnt_lst.append([j, i + 1])
                    cnt_lst.append([j + 1, i])
                    cnt_lst.append([j + 1, i + 1])
        unique_data = [list(x) for x in set(tuple(x) for x in cnt_lst)]
        cnt+=len(unique_data)

        #겹치는 부분이 없으면 리턴
        if len(cnt_lst) == 0:
            return cnt

        for i in unique_data: #사라진 위치의 값을 0으로 변환
            board[i[0]] = board[i[0]][:i[1]] + '0' + board[i[0]][i[1]+1:]

        #아래로 내려오게 해야해서 뒤집은 다음에 for 문 실행
        board.reverse()
        # 비어진 부분을 내리는 과정
        for j in range(m-1):
            for i in range(n):
                #0 인 부분이 나오면 그 위에 0 이 아닌 값을 찾아서 바꾼다
                if board[j][i] == '0':
                    for k in range(1,m-j):
                        if board[j+k][i] != '0':
                            board[j] = board[j][:i] + board[j+k][i] + board[j][i + 1:]
                            board[j+k] = board[j+k][:i] + '0' + board[j+k][i + 1:]
                            break

        board.reverse()
```
