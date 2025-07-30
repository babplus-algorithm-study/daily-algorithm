```python
H , W = map(int, input().split())
blocks = list(map(int, input().split()))

sum = 0

for i in range(1 ,len(blocks) - 1):
    left = max(blocks[:i])
    right = max(blocks[i:])

    rain = min(left ,right) - blocks[i]

    if rain > 0:
        sum += rain


print(sum)

```
