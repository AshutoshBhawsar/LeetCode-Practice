class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # hmap={x:s.count(x) for x in s}
        # for y in t:
        #     if y not in hmap or hmap[y]==0:
        #         return y
        #     hmap[y]-=1
        
        return (Counter(t) - Counter(s)).popitem()[0]
