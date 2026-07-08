from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [item for item, _ in counter.most_common(k)]
        

solution = Solution()
nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [1, 1, 5, 7, 8, 8, 8, 9, 0, 9, 9, 11, 11, 4, 6, 7]
k1 = 2
k2 = 3

print(solution.topKFrequent(nums1, k1))
print(solution.topKFrequent(nums2, k2))