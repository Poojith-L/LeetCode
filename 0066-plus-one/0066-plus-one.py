class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag=0
        i=len(digits)-1
        while i>=0:
            digits[i]+=1
            if digits[i]==10:
                digits[i]=0
            else:
                flag=1
                break
            i-=1
        if flag==0:
            digits.insert(0,1)
        return digits