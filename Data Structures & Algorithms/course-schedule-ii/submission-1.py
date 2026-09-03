class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen, visit = set(), set()
        res = []
        def dfs(crs):
            if crs in visit:
                return False
            if crs in seen:
                return True
            
            seen.add(crs)
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            res.append(crs)
            visit.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res