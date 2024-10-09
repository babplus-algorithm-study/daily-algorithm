```python
back_count = 0
menus = []
visit = []
answer = []
a_count = 0

def backtracking(x, u, orders):
    global back_count, answer, a_count
    
    if u == back_count:
        p_menu = []
        for v in range(len(visit)): # 코스 만들기
            if visit[v]:
                p_menu.append(menus[v])
                
        in_count = 0
        
        for order in orders: # 코스가 몇개의 주문에 포함되는지 체크
            signal = True
            for a in order:
                x_count = 0
                for b in p_menu:
                    if a == b:
                        x_count += 1
                if x_count == 0:
                    signal = False
                    break
            if signal:
                in_count += 1
        add_menu = "".join(p_menu)
        
        if in_count > a_count:
            answer = [add_menu]
            a_count = in_count
        elif in_count == a_count:
            answer.append(add_menu)
            return
        
    for v in range(x, len(visit)):
        visit[v] = True
        backtracking(x + 1, u + 1, orders)
        visit[v] = False
        
def solution(orders, course):
    global back_count, visit, a_count
    
    menus_set = set()
    for order in orders:
        for menu in order:
            menus_set.add(menu)
    
    for menu in menus_set:
        menus.append(menu)
    menus.sort()
    visit = [False for _ in range(len(menus))]
    ans = []
    
    for c in course:
        back_count = c
        a_count = 0
        
        backtracking(0, 0, orders)
        ans.extend(answer)
    ans.sort() 
    
    return ans
```