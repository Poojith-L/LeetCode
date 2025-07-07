class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=['#']
        v=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('(')
                v.append(1)
            else:
                if stack[-1]=='(':
                    stack.pop()
                    v.append(0)
                    for j in range(i-1,-1,-1):
                        if v[j]==1:
                            v[j]=0
                            break
                else:
                    stack.append(')')
                    v.append(1)
        c=0
        m=0
        for i in v:
            if i==0:
                c+=1
            else:
                if c>m:
                    m=c
                c=0
        if c>m:
            m=c
        return m