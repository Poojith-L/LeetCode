class Solution:
    def climbStairs(self, n: int) -> int:
        prev,curr=1,1
        for i in range(n-1):
            res=prev+curr
            prev=curr
            curr=res
        return curr