```python
from itertools import combinations

def solution(places):
    answer = []

    def check(case):
        for c in case:
            x1, y1 = c[0]
            x2, y2 = c[1]
            d = abs(x1 - x2) + abs(y1 - y2)
            if (d <= 2):
                if (x1 == x2):
                    if (map[x1][max(y1, y2) - 1] != 'X'):
                        return False
                elif (y1 == y2):
                    if (map[max(x1, x2) - 1][y1] != 'X'):
                        return False
                else:
                    if (map[x1][y2] != 'X') or (map[x2][y1] != 'X'):
                        return False

        return True

    for case in places:
        map = []
        for line in case:
            map.append(list(i for i in line))

        spot = []
        for row in range(5):
            for col in range(5):
                if (map[row][col] == 'P'):
                    spot.append([row, col])

        case = list(combinations(spot, 2))
        if check(case):
            answer.append(1)
        else:
            answer.append(0)

    return answer
```
