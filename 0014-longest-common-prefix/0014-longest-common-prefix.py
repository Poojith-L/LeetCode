class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=''
        if len(strs)==0:
            return s
        elif len(strs)==1:
            return strs[0]
        elif len(strs[0])<len(strs[1]):
            short=len(strs[0])
        else:
            short=len(strs[1])
        if short==0:
            return s
        for j in range(short):
            if strs[0][j]==strs[1][j]:
                s+=strs[0][j]
            else:
                break
        s1=''
        for i in range(1,len(strs)-1):
            if len(strs[i])<len(strs[i+1]):
                short=len(strs[i])
            else:
                short=len(strs[i+1])
            for j in range(short):
                if strs[i][j]==strs[i+1][j]:
                    s1+=strs[i][j]
                else:
                    break    
            if len(s)>len(s1):
                short=len(s1)
            else:
                short=len(s)
            s2=''
            for k in range(short):
                if s[k]==s1[k]:
                    s2+=s[k]
            s=s2
            s1=''
        return s
