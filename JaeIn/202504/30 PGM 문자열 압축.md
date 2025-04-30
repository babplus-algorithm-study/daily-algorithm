```python
def solution(s):
    n = len(s)
    answer = n


    for i in range(1 , n // 2 + 1):
        splited = []

        # 나눠서 배열에 저장
        for j in range(0, n, i):
            splited.append(s[j : j + i])

        count = 1
        # 압축된 문자열 저장 변수
        temp_str = ""
        for i in range(0 , len(splited) - 1):
            cur , next = splited[i] , splited[i + 1]
            if cur == next:
                count += 1
            else:
                if count == 1:
                    temp_str += cur
                else:
                    temp_str += f"{count}{cur}"
                count = 1

        # 마지막에 원소가 남았을 때
        if count == 1:
            temp_str += splited[-1]
        else:
            temp_str += f"{count}{splited[-1]}"

        answer = min(answer , len(temp_str))


    return answer

```
