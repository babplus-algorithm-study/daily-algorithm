import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    max_heap = []
    min_heap = []
    count_mp = defaultdict(int)
    
    for i in range(N):
        char, num = input().split()
        num = int(num)
        
        if char == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            count_mp[num] += 1
        
        elif char == 'D':
            if num == 1:
                while max_heap and count_mp[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    removed = -heapq.heappop(max_heap)
                    count_mp[removed] -= 1
            
            elif num == -1:

                while min_heap and count_mp[min_heap[0]] == 0:
                    heapq.heappop(min_heap)

                if min_heap:
                    removed = heapq.heappop(min_heap)
                    count_mp[removed] -= 1
    

    while max_heap and count_mp[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    while min_heap and count_mp[min_heap[0]] == 0:
        heapq.heappop(min_heap)


    if max_heap and min_heap:
        print(f"{-max_heap[0]} {min_heap[0]}")
    else:
        print("EMPTY")