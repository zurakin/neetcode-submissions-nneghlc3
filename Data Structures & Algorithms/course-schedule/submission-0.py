class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # for each index i -> which indices are blocked by i
        blocks = [[] for _ in range(numCourses)]

        # for each index i -> which indices block i
        blockedBy = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            blocks[b].append(a)
            blockedBy[a].append(b)

        toBeProcessed = []
        unblockedCount = 0
        for i in range(len(blockedBy)):
            if len(blockedBy[i]) == 0:
                toBeProcessed.append(i)
        
        while len(toBeProcessed) > 0:
            course = toBeProcessed.pop(0)
            unblockedCount += 1
            for dependentCourse in blocks[course]:
                blockedBy[dependentCourse].remove(course)
                if len(blockedBy[dependentCourse]) == 0:
                    toBeProcessed.append(dependentCourse)
        return unblockedCount == numCourses

