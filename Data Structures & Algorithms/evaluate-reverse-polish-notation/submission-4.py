class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: b-a,
            "*": lambda a, b: a*b,
            "/": lambda a, b: b/a
        }
        buffer = []
        for token in tokens:
            if token in operands:
                buffer.append(int(operands[token](buffer.pop(), buffer.pop())))
            else:
                buffer.append(int(token))
        return int(buffer[0])
