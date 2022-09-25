class Solution:
    def isValid(self, s: str) -> bool:
        hmap={'(':')','{':'}','[':']'}
        stack=[]
        for bracket in s:
            if bracket in hmap:
                stack.append(bracket)
            elif stack and hmap[stack.pop()]==bracket:
                continue
            else:
                return False
        return True if not stack else False
                