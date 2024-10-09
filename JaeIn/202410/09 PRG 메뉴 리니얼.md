```python
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for c in course:
        orders = sorted(orders)
        temp = []

        for o in orders:
            arr = list(combinations(o , c))
            temp.extend(arr)

        word_count = Counter(temp)
        if word_count:
            max_num = max(word_count.values())

            if max_num >= 2:
                for item , count in word_count.items():
                    if count == max_num:
                        result.append(''.join(item))

    return sorted(result)

```
