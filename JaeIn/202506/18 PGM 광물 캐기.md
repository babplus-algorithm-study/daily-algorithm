```python
def solution(picks, minerals):
    answer = 0


    temp_cnt = 0
    for p in picks:
        if p > 0:
            temp_cnt += p

    max_cnt = temp_cnt * 5
    minerals = minerals[:max_cnt]

    new_minerals = [[0,0,0] for _ in range((len(minerals) // 5) + 1)]

    # 광물을 채우기

    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1

    new_minerals.sort(key = lambda x : (-x[0] , -x[1] , -x[2]))

    for n in new_minerals:
        for j in range(len(picks)):
            d , i , s = n
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += d + i + s
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * d) + i + s
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * d) + (5 * i) + s
                break


    return answer
```
