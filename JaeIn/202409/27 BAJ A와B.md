```python
s = input()
t = input()
answer = False

def checkWord(word):
    return word == s

while len(t) > 0:
    if t[-1] == 'A':
        if checkWord(t[:-1]):
            answer = True
            break
        else:
            t = t[:-1]
    elif t[-1] == 'B':
        if checkWord(t[:-1][::-1]):
            answer = True
            break
        else:
            t = t[:-1][::-1]

print(1 if answer else 0)
```
