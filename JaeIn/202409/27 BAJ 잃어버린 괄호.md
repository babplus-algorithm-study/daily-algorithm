```python
str = input()
str = str.split('-')

result = 0

for i in range(len(str)):
    cur = sum(list(map(int , str[i].split('+'))))
    if i == 0:  result += cur
    else: result -= cur

print(result)
```
