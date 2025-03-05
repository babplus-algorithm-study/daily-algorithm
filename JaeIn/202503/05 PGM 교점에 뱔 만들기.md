```python
def solution(line):
    answer = []

    point = set()
    min_x , max_x , min_y , max_y = 0 , 0,  0 , 0

    for i in range(len(line)):
        for j in range(i + 1 , len(line)):
            a , b , e = line[i]
            c , d , f = line[j]

            if (a * d) - (b * c) != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)

                if int(x) == x and int(y) == y:
                    point.add((int(x) , int(y)))


    min_x = min(p[0] for p in point)
    max_x = max(p[0] for p in point)
    min_y = min(p[1] for p in point)
    max_y = max(p[1] for p in point)


    for y in range(max_y , min_y -1, -1):
        row = ""
        for x in range(min_x , max_x + 1):
            if (x , y) in point:
                row += "*"
            else:
                row += "."
        answer.append(row)

    return answer
```
