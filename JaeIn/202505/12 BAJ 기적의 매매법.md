```python
N = int(input())
price = list(map(int, input().split()))

# 준현이 전략 (BNP)
jun_cash = N
jun_cnt = 0

for p in price:
    if jun_cash >= p:
        buy = jun_cash // p
        jun_cnt += buy
        jun_cash -= buy * p

# 성민이 전략 (TIMING)
sung_cash = N
sung_cnt = 0

up = 0
down = 0

for i in range(1, len(price)):
    # 가격 상승 체크
    if price[i] > price[i - 1]:
        up += 1
        down = 0
    elif price[i] < price[i - 1]:
        down += 1
        up = 0
    else:
        up = 0
        down = 0

    # 매도 조건: 3일 연속 상승 → 다음날 하락 예상
    if up >= 3 and sung_cnt > 0:
        sung_cash += sung_cnt * price[i]
        sung_cnt = 0

    # 매수 조건: 3일 연속 하락 → 다음날 상승 예상
    elif down >= 3 and sung_cash >= price[i]:
        buy = sung_cash // price[i]
        sung_cnt += buy
        sung_cash -= buy * price[i]

# 마지막 자산 계산
jun_total = jun_cash + jun_cnt * price[-1]
sung_total = sung_cash + sung_cnt * price[-1]

if jun_total > sung_total:
    print("BNP")
elif jun_total < sung_total:
    print("TIMING")
else:
    print("SAMESAME")

```
