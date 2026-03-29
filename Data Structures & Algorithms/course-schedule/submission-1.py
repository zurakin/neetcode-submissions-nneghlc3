class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # for each index i -> which indices are blocked by i
        blocks = [[] for _ in range(numCourses)]

        # for each index i -> how many courses block i
        blockedBy = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            blocks[b].append(a)
            blockedBy[a] += 1

        toBeProcessed = []
        unblockedCount = 0
        for i in range(len(blockedBy)):
            if blockedBy[i] == 0:
                toBeProcessed.append(i)
        
        while len(toBeProcessed) > 0:
            course = toBeProcessed.pop(0)
            unblockedCount += 1
            for dependentCourse in blocks[course]:
                blockedBy[dependentCourse] -= 1
                if blockedBy[dependentCourse] == 0:
                    toBeProcessed.append(dependentCourse)
        return unblockedCount == numCourses

