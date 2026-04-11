def dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                heapq.heappush(distances, (dist(points[i], points[j]), i, j))
        
        representative = [i for i in range(len(points))]
        def getRepresentative(i):
            if representative[i] != i:
                representative[i] = getRepresentative(representative[i])
            return representative[i]

        def join(i, j) -> bool: # returns True if the join was successful and False if already joined
            iRep = getRepresentative(i)
            jRep = getRepresentative(j)
            if iRep == jRep:
                return False
            representative[jRep] = iRep
            return True

        edgesCount = 0
        res = 0
        while edgesCount < len(points)-1:
            distance, i, j = heapq.heappop(distances)
            if join(i, j):
                res += distance
                edgesCount += 1
        return res