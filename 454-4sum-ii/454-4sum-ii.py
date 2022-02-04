class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ht = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                ht[n1 + n2] += 1
        ans = 0
        c=0
        for n3 in nums3:
            for n4 in nums4:
                c=ht[-n3 - n4]
                ans +=c
        return ans