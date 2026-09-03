class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for pre in preMap[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return res if len(res) == numCourses else []