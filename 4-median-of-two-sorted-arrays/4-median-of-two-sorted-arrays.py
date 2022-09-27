class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        (small,big)=(nums1,nums2) if n>=m else (nums2,nums1)
        for item in small:
            big.insert(bisect.bisect(big,item),item)
        m_idx=((m+n)/2)-1
        if (m+n)%2==1:
            return float(big[ceil(m_idx)])
        return (big[int(m_idx)]+big[int(m_idx)+1])/2
        