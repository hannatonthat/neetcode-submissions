class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parMap = {i: i for i in range(n)}
        rank = [1] * n

        def find(x):
            while x != parMap[x]:
                parMap[x] = parMap[parMap[x]]
                x = parMap[x]
            return x
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parMap[p2] = p1
                rank[p1] += 1
            else:
                parMap[p1] = p2
                rank[p2] += 1
            
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
        
        return res

        
