class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap={}
        n1,n2=len(nums1),len(nums2)
        for i in range(n2):
            flag=False
            for j in range(i,n2):
                if nums2[j]>nums2[i]:
                    hmap[nums2[i]]=nums2[j]
                    flag=True
                    break
            if not flag:
                hmap[nums2[i]]=-1
                
        
        for k in range(n1):
            nums1[k]=hmap[nums1[k]]
        
        return nums1