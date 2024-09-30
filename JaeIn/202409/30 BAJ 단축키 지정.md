```python
n = int(input())
arr = [[] for _ in range(n)]
for i in range(n): arr[i] = input().split()

short_key = set()

for i in range(n):
    words = arr[i]
    found = False

    for j, word in enumerate(words):
        if word[0].upper() not in short_key and word[0].lower() not in short_key:
            words[j] = f"[{word[0]}]" + word[1:]
            short_key.add(word[0].upper())
            short_key.add(word[0].lower())
            found = True
            break

    if not found:
        for j, word in enumerate(words):
            for k in range(1, len(word)):
                if word[k].upper() not in short_key and word[k].lower() not in short_key:
                    words[j] = word[:k] + f"[{word[k]}]" + word[k+1:]
                    short_key.add(word[k].upper())
                    short_key.add(word[k].lower())
                    found = True
                    break
            if found:
                break

    arr[i] = " ".join(words)

for option in arr:
    print(option)

```
