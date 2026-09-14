from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        result = []

        for key, val in counter.items():
            if val >= k:
                result.append(key)
        
        return result