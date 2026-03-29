class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurences = {}
        for task in tasks:
            if task in occurences:
                occurences[task] += 1
            else:
                occurences[task] = 1

        heap = []
        for task, frequency in occurences.items():
            heapq.heappush(heap, (-frequency, task))
        queue = []
        t = 0
        while len(heap) > 0 or len(queue) > 0:
            t += 1
            if len(queue) > 0 and queue[0][1] == t: 
                heapq.heappush(heap, queue.pop(0)[0])
            if len(heap) > 0:
                f, task = heapq.heappop(heap)
                print(t, task)
                f *= -1
                f -= 1
                if f > 0:
                    queue.append(((-f, task), t+n+1))
            else: 
                if len(queue) > 0:
                    t = queue[0][1] -1
        return t
            

