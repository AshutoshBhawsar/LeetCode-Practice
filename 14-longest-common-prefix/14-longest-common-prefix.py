class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        flag=False
        temp=""
        for i in range(len(strs[0])):
            temp+=strs[0][i]
            for item in strs:
                if item.startswith(temp):
                    continue
                flag=True
            if flag:
                break
            else:
                result=temp
        return result