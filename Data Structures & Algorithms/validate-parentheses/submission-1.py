class Solution:
    def isValid(self, s: str) -> bool:
        inverses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        queue = []
        for p in s:
            if p in ['(', '{', '[']:
                queue.append(p)
            elif len(queue) > 0 and inverses[queue[-1]] == p:
                queue.pop()
            else: 
                return False 
        return len(queue) == 0