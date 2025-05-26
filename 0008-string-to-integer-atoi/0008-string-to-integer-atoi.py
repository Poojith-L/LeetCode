class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        j=0
        if len(s)==0 or (s[0].isdigit()==False and len(s)==1):
            return 0
        elif s[0].isdigit():
            for i in s:
                if i.isdigit()!=True:
                    break
                else:
                    j+=1
        elif (s[0]=='-' or s[0]=='+') and s[1].isdigit():
            for i in s[1:]:
                if i.isdigit()!=True:
                    break
                else:
                    j+=1
            j+=1
        else:
            return 0
        x=int(s[:j])
        int_min=-2**31
        int_max=2**31-1
        return max(int_min, min(int_max, x))