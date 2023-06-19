class HitCounter:

    def __init__(self):
        self.queue=collections.deque([])

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while(self.queue):
            tminus=timestamp-self.queue[0]
            if tminus>=300:
                self.queue.popleft()
            else:
                break
        return len(self.queue)
                

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)