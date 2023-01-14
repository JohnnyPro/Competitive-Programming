class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        innerStack = []

        for i in s:
            if i == ')':
                j = stack.pop()
                while j != '(':
                    innerStack.append(j)
                    j = stack.pop()

                while innerStack:
                    stack.append(innerStack.pop(0))
            
            else:
                stack.append(i)

        return ''.join(stack)