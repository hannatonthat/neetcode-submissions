class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, des in sorted(tickets)[::-1]:
            adj[src].append(des)

        res = []
        def dfs(src):
            while adj[src]:
                des = adj[src].pop()
                dfs(des)
            res.append(src)

        dfs("JFK")
        return res[::-1]