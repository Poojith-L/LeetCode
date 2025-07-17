class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r=[]
        i=j=nums[0]
        for n in nums[1:]:
            if (j+1)==n:
                j=n
            else:
                if i==j:
                    r.append(str(i))
                else:
                    r.append(str(i)+"->"+str(j))
                i=j=n
        if i==j:
            r.append(str(i))
        else:
            r.append(str(i)+"->"+str(j))
        return r


