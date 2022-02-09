class MinStack(object):

    def __init__(self):
        self.object=[]
        #self.current_min=float('inf')
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.object:
            self.object.append((val,val))
            return
        current_min=self.object[-1][1]
        self.object.append((val,min(val,current_min)))
        # if val<self.current_min:
        #     self.current_min=val
        # self.object.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.object.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.object[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.object[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()