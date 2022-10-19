class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals=sorted(intervals, key=lambda x:x[0])
        answer=[new_intervals[0]]
        for curr in new_intervals[1:]:
            prev=answer[-1]
            if prev[1]>=curr[0]:
                answer.pop()
                answer.append([prev[0],max(prev[1],curr[1])])
                continue
            else:
                answer.append(curr)
        return answer