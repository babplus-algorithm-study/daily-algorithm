```python
def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        st = h*60+m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x:x[1])
    stack = []

    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break

        name, st, t = plans[i]
        next_name , next_st , next_t = plans[i + 1]

        # 과제에서 진행까지 했을 때 다음 과제 시작시간보다 작을 경우
        if st + t <= next_st:
            answer.append(name)
            gap = next_st - (st + t)

            while gap > 0 and len(stack):
                s_name ,s_st , s_t = stack.pop()
                if gap >= s_t:
                    answer.append(s_name)
                    gap -= s_t
                else:
                    s_t -= gap
                    stack.append([s_name , s_st , s_t])
                    gap = 0

        # 다음 과제 시작시간이 더  경우
        else:
            t -= next_st - st
            stack.append([name, st, t])


    while stack:
        s_name ,s_st , s_t = stack.pop()
        answer.append(s_name)

    return answer
```
