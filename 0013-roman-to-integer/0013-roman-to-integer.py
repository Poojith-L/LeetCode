class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        revstr=list(s)[::-1]
        value=0
        r=roman_dict[revstr[0]]
        for i in revstr:
            l=roman_dict[i]
            if l<r:
                value-=l
            else:
                value+=l
                r=l
        return value
