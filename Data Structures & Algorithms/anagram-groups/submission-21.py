from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagrams[sorted_s].append(s)
        
        result = []

        for _, val in anagrams.items():
            result.append(val)
        
        return result