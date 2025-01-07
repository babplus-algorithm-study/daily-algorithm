```python
def solution(book_time):
    answer = 0
    room = []

    new_book_time = [[0, 0] for _ in range(len(book_time))]
    for idx, (s, e) in enumerate(book_time):
        ns = list(map(int, s.split(":")))
        ne = list(map(int, e.split(":")))

        new_book_time[idx][0] = ns[0] * 60 + ns[1]
        new_book_time[idx][1] = ne[0] * 60 + ne[1]

    new_book_time.sort(key=lambda x: x[0])

    room.append(new_book_time[0][1] + 10)

    for i in range(1, len(new_book_time)):
        s, e = new_book_time[i]
        flag = False

        for j in range(len(room)):
            if s >= room[j]:
                flag = True
                room[j] = e + 10
                break

        if not flag:
            room.append(e + 10)


    return len(room)


```
