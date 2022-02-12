class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [len(list(num)) for _, num in itertools.groupby(s)]
    
        sum1=0
        j=1
        for i in range(len(groups)-1):
            sum1+=min(groups[i],groups[j])
            j+=1
        return sum1

        #return sum(min(a, b) for a, b in zip(groups, groups[1:]))