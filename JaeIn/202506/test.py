n, k = map(int, input().split())

# 체스판 정보 입력
chess_map = []
for i in range(n):
    chess_map.append(list(map(int, input().split())))

# 말의 위치와 방향 정보 입력
start_horse_location_and_directions = []
for i in range(k):
    r, c, d = map(int, input().split())
    start_horse_location_and_directions.append([r-1, c-1, d-1])  # 0-based 인덱스로 변환

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    
    # 초기 말 위치 설정
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    
    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            
            # 파란색이거나 체스판을 벗어나는 경우
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                
                # 방향을 바꾼 후에도 파란색이거나 벗어나면 이동하지 않음
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue
            
            # 이동할 말들 찾기 (현재 말과 그 위의 모든 말들)
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break
            
            # 빨간색인 경우 순서 뒤집기
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = list(reversed(moving_horse_index_array))
            
            # 말들을 새 위치로 이동
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                # 말들의 위치 정보 업데이트
                horse_location_and_directions[moving_horse_index][0] = new_r
                horse_location_and_directions[moving_horse_index][1] = new_c
            
            # 게임 종료 조건 확인 (4개 이상 쌓임)
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        
        turn_count += 1
    
    return -1

# 결과 출력
result = get_game_over_turn_count(k, chess_map, start_horse_location_and_directions)
print(result)