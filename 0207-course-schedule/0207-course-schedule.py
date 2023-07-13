class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        in_degrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degrees[course] += 1

        queue = deque()

        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            numCourses -= 1

            for neighbor in graph[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == 0