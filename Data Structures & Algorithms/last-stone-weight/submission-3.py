class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        freq = [0] * (max(stones) + 1)

        for s in stones:
            freq[s] += 1
        
        first, second = max(stones), max(stones)
        while first > 0:
            if freq[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            while j > 0 and freq[j] == 0:
                j -= 1
            if j == 0:
                return first
            second = j
            freq[first] -= 1
            freq[second] -= 1
            freq[first - second] += 1
            first = max(first - second, second)
            
        return first
        
        