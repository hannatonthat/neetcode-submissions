class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                adj[pattern].append(w)
        
        q = deque([beginWord])
        res = 1
        seen = set([beginWord])
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        
        return 0