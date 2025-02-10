```python
def solution(diffs, times, limit):
    answer = 0

    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2

        if cal(diffs, times, limit, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def cal(diffs, times, limit, level):
    time_added = 0

    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_pre = 0
        if i != 0:
            time_pre = times[i - 1]

        if diff <= level:
            time_added += time_cur
        else:
            re_cnt = diff - level
            re_cal = time_pre + time_cur
            cal_time = re_cnt * re_cal + time_cur
            time_added += cal_time

        if time_added > limit:
            return False

    return True
```
