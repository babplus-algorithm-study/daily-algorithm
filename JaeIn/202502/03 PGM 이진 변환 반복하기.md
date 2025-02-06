```python
def solution(s):
    count_zero = 0
    count_binary = 0

    while s != '1':
        count_zero += s.count('0')
        s = s.replace('0', '')

        c = len(s)
        binary_str = ''

        while c > 0:
            binary_str += str(c % 2)
            c //= 2

        s = binary_str[::-1]
        count_binary += 1

    return [count_binary, count_zero]
```
