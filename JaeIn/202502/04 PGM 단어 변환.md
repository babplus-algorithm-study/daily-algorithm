```python

from collections import deque

def checkWord(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]: count+=1

    if count > 1:
        return False
    return count == 1

def bfs(begin, target, words):
    if target not in words: return 0

    queue = deque([(begin, 0)])
    visited = set([begin])
    while queue:
        cur , value = queue.popleft()
        if cur == target: return value

        for word in words:
            if checkWord(cur , word) and word not in visited:
                queue.append((word , value + 1))
                visited.add(word)
    return 0

def solution(begin, target, words):
    return bfs(begin, target, words)



```
