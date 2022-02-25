class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        h = collections.defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            h[rings[i + 1]].add(rings[i])
        return sum(len(v) == 3 for v in h.values())