class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)
        res = []
        visited = set()

        def dfs(i, being_visited):
            if i in being_visited:
                return False
            if i in visited:
                return True
            visited.add(i)
            being_visited.add(i)
            for j in graph[i]:
                if not dfs(j, being_visited):
                    return False
            being_visited.remove(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        return res[::-1]
