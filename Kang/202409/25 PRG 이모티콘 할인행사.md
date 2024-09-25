```python
e_count = 0
percents = []
u = []
e = []
max_count = [0, 0]
def calcurate():
    global e_count, percents, u, e, max_count
    partial_count = [0, 0]
    for (a, b) in u:
        min_cost = 0
        for i in range(e_count):
            if a <= percents[i]:
                min_cost += int((e[i] * (100 - percents[i])) / 100) # 정답
                # min_cost += int(e[i] * ((100 - percents[i]) / 100)) # 오답
        if b <= min_cost:
            partial_count[0] += 1
        else:
            partial_count[1] += min_cost
    return partial_count

def back_track(c):
    global e_count, percents, u, e, max_count
    if (e_count == c):
        p_count = calcurate()
        if max_count[0] < p_count[0]:
            max_count = p_count
        elif max_count[0] == p_count[0]\
        and max_count[1] < p_count[1]:
            max_count = p_count
        return
    for i in range(10, 50, 10):
        percents[c] = i
        back_track(c + 1)
    
def solution(users, emoticons):
    global e_count, percents, u, e, max_count
    
    e_count = len(emoticons)
    percents = [0 for _ in range(e_count)]
    u = users
    e = emoticons
    
    back_track(0)

    return max_count
```