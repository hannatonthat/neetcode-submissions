class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        res = 0
        while q:
            crs = q.popleft()
            res += 1
            for pre in preMap[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return res == numCourses