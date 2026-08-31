class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        seen, visiting = set(), set()

        def dfs(crs):
            if crs in seen:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            seen.add(crs)
            output.append(crs)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return output