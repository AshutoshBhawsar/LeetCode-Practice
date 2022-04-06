class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        freq=collections.defaultdict(int)

        def isValid(freq):
            return (freq['c']>=freq['r'] and
                    freq['r']>=freq['o'] and
                    freq['o']>=freq['a'] and
                    freq['a']>=freq['k'])

        frogs = 0
        answer = -1
        for ch in croakOfFrogs:
            freq[ch]+=1

            if (not isValid(freq)):
                return -1

            if ch=='c':
                frogs+=1

            if ch=='k':
                frogs-=1

            answer=max(answer,frogs)

        if frogs==0:
            return answer

        return -1