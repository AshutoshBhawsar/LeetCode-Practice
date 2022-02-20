class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # brute force############
#         c=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 c+=1
#             if k==c:
#                 return i
        
#         return -1

        # math upto sqrt(n) and save 2 divisors in 1 successful division 
        f1, f2 = [], []
        for s in range(1, int(sqrt(n)) + 1 ):
            if n % s == 0:
                f1 += [s]
                f2 += [n//s]
                
        if f1[-1] == f2[-1]: f2.pop() #perfect square condition hence eliminate 1 entry
            
        factors = f1 + f2[::-1]
        return -1 if len(factors) < k else factors[k-1]
        