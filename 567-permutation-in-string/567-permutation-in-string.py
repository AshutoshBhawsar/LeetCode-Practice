class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Brute Force approach ############### TLE
        # perm=itertools.permutations(s1)
        # l1=[]
        # for i in perm:
        #     l1.append(''.join(x for x in i))
        # for item in l1:
        #     if item in s2:
        #         return True
        # return False
        
        
        
        # SLiding Window ###################
        
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
    
        