class Solution:
    def hasDuplicate(self, nums: list[int], x: int = None) -> list[int]:
        return len(nums) != len(set(nums))
solution = Solution()
nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [1,2,3,4,5,6,7,8,9,10,1]
ans1 = solution.hasDuplicate(nums1)
ans2 = solution.hasDuplicate(nums2)
print(ans1)
print(ans2)