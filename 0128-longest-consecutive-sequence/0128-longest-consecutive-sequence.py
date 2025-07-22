class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        lces=count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]-1:
                count+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                if lces<count:
                    lces=count
                count=0
        if lces<count:
            lces=count
        return lces+1