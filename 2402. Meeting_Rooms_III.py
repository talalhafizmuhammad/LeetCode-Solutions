import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        
        available = list(range(n))
        heapq.heapify(available)
        
        ongoing = []
        
        count = [0] * n
        
        for start, end in meetings:
            while ongoing and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)
            
            duration = end - start
            if available:
                room = heapq.heappop(available)
                heapq.heappush(ongoing, (end, room))
                count[room] += 1
            else:
                end_time, room = heapq.heappop(ongoing)
                heapq.heappush(ongoing, (end_time + duration, room))
                count[room] += 1
        
        return count.index(max(count))
