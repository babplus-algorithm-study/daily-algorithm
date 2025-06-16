from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append([brown_loc , 0])
    visited = [{} for _ in range(200001)]
    
    while cony_loc <= 200000:
        # 코니의 위치   
        cony_loc += time
        
        
        if time in visited[cony_loc]:
            return time
        
        
        for _ in range(len(queue)):
            cur_pos , cur_time = queue.popleft()
            cur_time += 1
            
            cur_pos += 1
            if cur_pos <= 200000:
                visited[cur_pos][cur_time] = True
                queue.append([cur_pos , cur_time])
            
            cur_pos -= 1
            if cur_pos >= 200000:
                visited[cur_pos][cur_time] = True
                queue.append([cur_pos , cur_time])
            
            cur_pos *= 2
            if cur_pos <= 200000:
                visited[cur_pos][cur_time] = True
                queue.append([cur_pos , cur_time])
    
        
        time += 1
    return False


print(catch_me(c, b))  # 5가 나와야 합니다!
