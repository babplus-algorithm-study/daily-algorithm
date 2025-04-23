```
def solution(s):
    answer = []
    l = len(s)
    if l == 1:
        return 1

    for i in range(1 , l//2 + 1):
        result = ""
        temp = s[:i]
        cnt = 1

        for j in range(i , l , i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + temp
                else:
                    result += temp

                temp = s[j:j+i]
                cnt = 1

        if cnt > 1:
            result += str(cnt) + temp
        else:
            result += temp
        answer.append(len(result))

    return min(answer)
```
