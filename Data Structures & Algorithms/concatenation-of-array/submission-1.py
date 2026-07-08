class Solution:
    def getConcatenation(self, nums: list[int], x: int = None) -> list[int]:
        if x is not None:
            return nums * x
        return nums + nums
solution = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
ans = solution.getConcatenation(nums)

print(nums)
print(ans)
n = len(nums)
i = 4
print(ans[i] == nums[i])
print(ans[i+n]== nums[i])