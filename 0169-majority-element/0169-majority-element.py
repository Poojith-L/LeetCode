class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        prev=m=nums[0]
        maxi=0
        for i in nums[1:]:
            if prev==i:
                count+=1
            else:
                count=1
            prev=i
            if count>maxi:
                maxi=count
                m=i
        return m
