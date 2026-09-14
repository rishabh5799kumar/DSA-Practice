from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        result = []

        for key, val in counter.items():
            result.append([val, key])
        
        heapq.heapify(result)

        while len(result) > k:
            heapq.heappop(result)
        
        return[val for _, val in result]