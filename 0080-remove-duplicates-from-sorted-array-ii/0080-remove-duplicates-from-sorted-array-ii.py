class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=nums[0]
        count=0
        i=1
        while i<len(nums):
            if prev==nums[i]:
                count+=1
            else:
                count=0
            prev=nums[i]
            if count>1:
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)