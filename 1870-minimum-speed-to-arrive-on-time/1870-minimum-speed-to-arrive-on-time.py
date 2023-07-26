class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def is_possible(speed):
            total_time = 0
            n = len(dist)
            for i in range(n - 1):
                total_time += (dist[i] + speed - 1) // speed
            total_time += dist[-1] / speed
            return total_time <= hour

        left, right = 1, 10**7
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid - 1
            else:
                left = mid + 1

        if is_possible(left):
            return left
        return -1