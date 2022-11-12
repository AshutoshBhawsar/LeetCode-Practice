class MedianFinder:
    
    def __init__(self):
        from sortedcontainers import SortedList
        self.sorted_list=SortedList()
        self.num_count=0

    def addNum(self, num: int) -> None:
        self.sorted_list.add(num)
        self.num_count+=1

    def findMedian(self) -> float:
        mid=self.num_count//2
        if self.num_count%2==0:
            return (self.sorted_list[mid-1]+self.sorted_list[mid])/2
        else:
            return self.sorted_list[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()