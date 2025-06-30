class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=[]
        for i in nums1:
            s.append(i)
        for i in nums2:
            s.append(i)
        s.sort()
        n=len(nums1)+len(nums2)
        if n%2==0:
            a=int(n/2)
            b=a-1
            m=(s[a]+s[b])/2
        else:
            a=int((n-1)/2)
            m=s[a]
        return m