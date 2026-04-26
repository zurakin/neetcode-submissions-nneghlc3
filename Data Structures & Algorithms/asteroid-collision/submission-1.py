class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        res = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                destroyed = False
                while stack:
                    if stack[-1] == abs(a):
                        stack.pop()
                        destroyed = True
                        break
                    if stack[-1] > abs(a):
                        destroyed = True
                        break
                    stack.pop()
                if not destroyed:
                    res.append(a)
        return res+list(stack)
