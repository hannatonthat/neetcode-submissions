class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_count(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            return count
        
        hash_map = defaultdict(list)

        for s in strs:
            count = get_count(s)
            hash_map[tuple(count)].append(s)
        
        return list(hash_map.values())