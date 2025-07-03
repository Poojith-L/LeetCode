class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m=len(a)-1
        n=len(b)-1
        s=""
        r=''
        c=0
        while(1):
            if int(a[m])+int(b[n])==0:
                if c==0:
                    r='0'
                else:
                    r='1'
                    c=0
            elif int(a[m])+int(b[n])==1:
                if c==0:
                    r='1'
                else:
                    r='0'
                    c=1
            else:
                if c==0:
                    r='0'
                else:
                    r='1'
                c=1
            s=r+s
            if m==0:
                m=-1
                n-=1
                break
            if n==0:
                n=-1
                m-=1
                break
            m-=1
            n-=1
        for i in range(m,-1,-1):
            if int(a[i])==0:
                if c==0:
                    r='0'
                else:
                    r='1'
                    c=0
            else:
                if c==0:
                    r='1'
                else:
                    r='0'
                    c=1
            s=r+s
        for i in range(n,-1,-1):
            if int(b[i])==0:
                if c==0:
                    r='0'
                else:
                    r='1'
                    c=0
            else:
                if c==0:
                    r='1'
                else:
                    r='0'
                    c=1
            s=r+s
        if c==1:
            s='1'+s
        return s