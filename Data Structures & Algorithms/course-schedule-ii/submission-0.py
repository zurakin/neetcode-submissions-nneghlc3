class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # for each index i -> which indices are blocked by i
        blocks = [[] for _ in range(numCourses)]

        # for each index i -> how many courses block i
        blockedBy = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            blocks[b].append(a)
            blockedBy[a] += 1

        toBeProcessed = []
        unblocked = []
        for i in range(len(blockedBy)):
            if blockedBy[i] == 0:
                toBeProcessed.append(i)
        
        while len(toBeProcessed) > 0:
            course = toBeProcessed.pop(0)
            unblocked.append(course)
            for dependentCourse in blocks[course]:
                blockedBy[dependentCourse] -= 1
                if blockedBy[dependentCourse] == 0:
                    toBeProcessed.append(dependentCourse)
        return unblocked if len(unblocked) == numCourses else []