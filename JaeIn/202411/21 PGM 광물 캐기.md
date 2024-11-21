```python
def solution(picks, minerals):
    answer = 0
    sum = 0
    for x in picks:
        sum += x

    num_min = sum * 5
    if len(minerals) > num_min:
        minerals = minerals[:num_min]

    cnt_min = [[0, 0, 0]for x in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron':
            cnt_min[i//5][1] += 1
        else :
            cnt_min[i//5][2] += 1

    # 내림차순 정렬
    # 다이아 -> 철 -> 돌 순으로 처리를 먼저하기 위해 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))

    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0:
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0:
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0:
                picks[p]-=1
                answer += 25*d + 5*i + s
                break

    return answer
```
