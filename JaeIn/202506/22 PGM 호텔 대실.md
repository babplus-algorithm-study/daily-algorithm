```python
def solution(book_time):
    room = []
    time = []

    # 시간을 분 단위로 변환
    for b in book_time:
        s, e = b
        s_h, s_m = map(int, s.split(":"))
        e_h, e_m = map(int, e.split(":"))
        time.append([s_h * 60 + s_m, e_h * 60 + e_m])

    # 시작 시간을 기준으로 정렬
    time.sort(key=lambda x: x[0])

    for t in time:
        s, e = t

        # 사용 가능한 방 찾기 (가장 빨리 사용 가능한 방)
        available_room = -1
        earliest_time = float('inf')


        for i in range(len(room)):
            if room[i] <= s and room[i] < earliest_time:
                available_room = i
                earliest_time = room[i]

        # 사용 가능한 방이 있으면 업데이트, 없으면 새 방 추가
        if available_room != -1:
            room[available_room] = e + 10
        else:
            room.append(e + 10)

    return len(room)
```
