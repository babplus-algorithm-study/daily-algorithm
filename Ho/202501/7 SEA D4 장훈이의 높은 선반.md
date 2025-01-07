```python
import itertools

t = int(input())

for tt in range(1,t+1):
    minValue = 10000000
    n, b = map(int, input().split())

    arr = list(map(int, input().split()))
    for i in range(1,len(arr)+1):
        list1 = itertools.combinations(arr, i)

        for i in list1:
            sum = 0

            for j in i:
                sum += j

            if(sum >= b and sum < minValue):
                minValue = sum

    print(f"#{tt} {minValue - b}")
```