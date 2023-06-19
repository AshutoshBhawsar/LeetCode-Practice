class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        result_str=""
        num=0
        
        for ch in s:
            if ch=='[':
                stack.append((result_str,num))
                result_str=""
                num=0
            elif ch==']':
                last_string, last_num=stack.pop(-1)
                result_str=last_string+last_num*result_str
            elif ch.isdigit():
                num=num*10+int(ch)
            else:
                result_str+=ch
        return result_str
            