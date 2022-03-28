class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        for ch in s:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)