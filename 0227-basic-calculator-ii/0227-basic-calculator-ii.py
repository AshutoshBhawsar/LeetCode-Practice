class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        operator="+"
        current=0
        i=0
        
        def update(operator, value):
            if operator=="+": stack.append(value)
            elif operator=="-": stack.append(-value)
            elif operator=="*": stack.append(stack.pop()*value)
            else: stack.append(int(stack.pop()/value))
        
        while(i<len(s)):
            if s[i].isdigit():
                current=current*10+int(s[i])
            elif s[i] in "+*/-":
                update(operator,current)
                current=0
                operator=s[i]
            i+=1
        update(operator,current)
        return sum(stack)
