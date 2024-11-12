```python
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

dice = list(map(int, input().split()))
answer = 0


def backtracking(depth, result, horses):
    global answer
    if depth == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        x = horses[i]

        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]

        for _ in range(1, dice[depth]):
            x = graph[x][0]

        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  
            horses[i] = x  

            backtracking(depth + 1, result + score[x], horses)

            horses[i] = before


backtracking(0, 0, [0, 0, 0, 0])
print(answer)
```