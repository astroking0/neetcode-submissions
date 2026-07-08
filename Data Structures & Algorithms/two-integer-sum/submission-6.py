from collections import Counter
from typing import List
import random

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # {القيمة: المؤشر}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []
            
solution = Solution()
nums = [random.randint(1, 1000) for _ in range(100)]
print(solution.twoSum(nums, 136))
print(len(nums))