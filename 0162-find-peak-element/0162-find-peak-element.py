class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
        if len(nums)==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return len(nums)-1