class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=j=0
        k=m
        while j<n:
            if nums1[i]>=nums2[j]:
                nums1.insert(i,nums2[j])
                j+=1
                k+=1
            elif i<k:
                i+=1    
            else:
                nums1[i:]=nums2[j:]  
                break
        nums1[m+n:]=[]