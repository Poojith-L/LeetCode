class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1+op2)
            elif i=='-':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1-op2)
            elif i=='*':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1*op2)
            elif i=='/':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(int(op1/op2))
            else:
                stack.append(int(i))
        return stack[0]