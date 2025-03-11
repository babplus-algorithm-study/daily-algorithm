```python
def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''

        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
            elif not number:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(s) for s in answer]
```
