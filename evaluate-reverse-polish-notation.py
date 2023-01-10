class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "*" or i =="-" or i == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                if i == '+': stack.append(first + second)
                elif i == '-': stack.append(first - second)
                elif i == '*': stack.append(first * second)
                else: stack.append(first / second)
               
            else:
                stack.append(i)
        return int(stack.pop())
