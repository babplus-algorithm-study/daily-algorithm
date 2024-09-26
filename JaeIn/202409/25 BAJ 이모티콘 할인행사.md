```python
def solution(users, emoticons):
    answer = [0, 0]
    rate = [10, 20, 30, 40]
    discount = []

    def dfs(temp , depth):
        if depth == len(temp):
            discount.append(temp[:])
            return

        for r in rate:
            temp[depth] += r
            dfs(temp , depth + 1)
            temp[depth] -= r

    dfs([0] * len(emoticons) , 0)

    for r in range(len(discount)):
        plus_count = 0
        sum_price = 0

        for user in users:
            price = 0
            for i in range(len(emoticons)):
                if discount[r][i] >= user[0]:
                    price += emoticons[i] * ((100 - discount[r][i]) / 100)

            if price >= user[1]: plus_count += 1
            else: sum_price += price


        if answer[0] < plus_count:
            answer = [plus_count , sum_price]
        elif answer[0] == plus_count:
            if answer[1] < sum_price:
                answer = [plus_count , sum_price]


    return answer
```
