class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parMap = {i: i for i in range(len(edges) + 1)}
        rank = [1] * (len(edges) + 1)

        def find(x):
            while x != parMap[x]:
                parMap[x] = parMap[parMap[x]]
                x = parMap[x]
            return x
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parMap[p2] = p1
                rank[p1] += 1
            else:
                parMap[p1] = p2
                rank[p2] += 1
            
            return True
        
        res = [-1, -1]
        for u, v in edges:
            if not union(u, v):
                res = [u, v]
        
        return res

        
