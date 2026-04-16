class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        time = 0
        current = 0
        cpuHeap = []
        res = []
        while current < len(tasks) or cpuHeap:
            if current < len(tasks) and tasks[current][0] > time:
                time = tasks[current][0]
            while current < len(tasks) and time >= tasks[current][0]:
                heapq.heappush(cpuHeap, (tasks[current][1], tasks[current][2]))
                current += 1
            if cpuHeap:
                duration, taskToProcess = heapq.heappop(cpuHeap)
                res.append(taskToProcess)
                time += duration
        return res

            