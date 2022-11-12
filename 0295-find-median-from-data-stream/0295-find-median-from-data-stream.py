from heapq import *
class MedianFinder:
    
    # Sorted List built in data structure O(n)
#     def __init__(self):
#         from sortedcontainers import SortedList
#         self.sorted_list=SortedList()
#         self.num_count=0

#     def addNum(self, num: int) -> None:
#         self.sorted_list.add(num)
#         self.num_count+=1

#     def findMedian(self) -> float:
#         mid=self.num_count//2
#         if self.num_count%2==0:
#             return (self.sorted_list[mid-1]+self.sorted_list[mid])/2
#         else:
#             return self.sorted_list[mid]

    # Heap
    # Max-heap small has the smaller half of the numbers.
    # Min-heap large has the larger half of the numbers.
    # Credits: https://leetcode.com/StefanPochmann
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()