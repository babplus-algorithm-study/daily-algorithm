```python
def solution(N, number):
    if N == number:
        return 1

    answer = -1
    arr = [set() for _ in range(8)]

    for i in range(len(arr)):
        arr[i].add(int(str(N) * (i + 1)))

    for i in range(1 , 8):
        for j in range(i):
            for a in arr[j]:
                for b in arr[i - j - 1]:
                    print(a , b)
                    arr[i].add(a + b)
                    arr[i].add(a - b)
                    arr[i].add(a * b)
                    if b != 0:
                        arr[i].add(a // b)

        if number in arr[i]:
            answer = i + 1
            break

    return answer
```
