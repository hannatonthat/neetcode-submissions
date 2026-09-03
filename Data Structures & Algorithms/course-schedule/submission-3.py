class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen, visiting = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in seen:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            seen.add(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True