```python
import math

def solution(fees, records):
    park_d = dict()
    d = dict()

    for record in records:
        time, num, check = record.split()
        h, m = map(int, time.split(":"))
        time_minutes = h * 60 + m

        if check == 'IN':
            d[num] = time_minutes
            if num not in park_d:
                park_d[num] = 0
        elif check == 'OUT':
            if num in d:
                parked_time = time_minutes - d[num]
                park_d[num] += parked_time
                del d[num]


    for num, time in d.items():
        parked_time = (23 * 60 + 59) - time
        park_d[num] += parked_time

    price = {}
    for num, total_time in park_d.items():
        if total_time <= fees[0]:
            price[num] = fees[1]
        else:
            extra_time = total_time - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]
            price[num] = fees[1] + extra_fee

    return [price[num] for num in sorted(price.keys())]

```
