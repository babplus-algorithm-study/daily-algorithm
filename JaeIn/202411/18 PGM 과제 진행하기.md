```python
def change_time(time):
    hours, minutes = map(int,time.split(':'))
    return int(minutes + (hours*60))

def solution(plans):
    answer = []
    left_table = []
    left_time = 0
    for plan in plans:
        plan[1] = change_time(plan[1])
    plans.sort(key=lambda x: x[1])

    for i, (plan_1, plan_2) in enumerate(zip(plans, plans[1:])):
        pred_end, tail_start = plan_1[1]+int(plan_1[2]), plan_2[1]

        if pred_end > tail_start:
            left_table.append([plan_1[0], pred_end - tail_start])
        else:
            answer.append(plan_1[0])
            left_time = tail_start - pred_end

            while left_time > 0:
                if left_table:
                    plan = left_table.pop()
                    left_time = left_time - plan[1]
                else:
                    break

                if left_time >= 0 :
                    answer.append(plan[0])
                else:
                    plan[1] = -left_time
                    left_table.append(plan)

    answer.append(plans[-1][0])
    while left_table:
        answer.append(left_table.pop()[0])

    return answer
```
