```python
parentheses = list(input())
stack = []
answer= 0
temp = 1

for i, p in enumerate(parentheses):
    if p == '(':
        stack.append(p)
        temp *= 2
    elif p == "[":
        stack.append(p)
        temp *= 3
    elif p == ")":
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if parentheses[i-1] == "(":
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if parentheses[i-1] == "[":
            answer += temp

        stack.pop()
        temp //= 3


if stack:
    print(0)
else:
    print(answer)
```
