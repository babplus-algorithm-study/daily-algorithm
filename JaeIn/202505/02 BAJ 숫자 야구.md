```python
import sys
input = sys.stdin.readline

n = int(input())
answer = 0

arr = []
for _ in range(n):
    arr.append(list(map(int , input().split())))


for i in range(1 , 10):
    for j in range(1 , 10):
        for k in range(1 , 10):

            # 모두 다른 수만 가능
            if i == j or j == k or i == k:
                continue

            cnt = 0
            for a in arr:
                num = str(a[0])
                strike = a[1]
                ball = a[2]

                strike_cnt = 0
                ball_cnt = 0

                checkNum = str(i) + str(j) + str(k)
                # 볼 , 스트라이크 체크
                for t in range(3):
                    if num[t] == checkNum[t]:
                        strike_cnt += 1
                    elif num[t] in checkNum:
                        ball_cnt += 1

                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1

            if cnt == n:
                answer += 1


print(answer)






```
