class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        d={0:1}
        for i in nums:
            sum+=i
            if d.get(sum-k):
                count+=d.get(sum-k)
                d[sum-k]=d.get(sum-k)+1
            d.setdefault(sum,1)
        return count