class Solution(object):
    def reorganizeString(self, S):
        """
        :type s: str
        :rtype: str
        """
        s, l = list(S), len(S)
        ct = collections.Counter(s)
        #cannot only sort by ct[x], "abbabbaaab" is the edge case
        #when ct[x] equals, have to sort by alpha, otherwise it is a mess
        s.sort(key=lambda x: (ct[x], x), reverse=True)
        if ct[s[0]] > (l + 1) // 2: return ''
        rst, iters = [None] * l, iter(s)
        for i in range(0, l, 2): rst[i] = next(iters)
        for i in range(1, l, 2): rst[i] = next(iters)
        return ''.join(rst)