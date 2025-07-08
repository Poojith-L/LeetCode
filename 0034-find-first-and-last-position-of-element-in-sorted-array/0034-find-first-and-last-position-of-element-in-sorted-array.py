class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flag=0
        f,l=-1,-1
        for i in range(len(nums)):
            if nums[i]==target and flag==0:
                f,l=i,i
                flag=1
            elif nums[i]==target:
                l=i
        return [f,l]