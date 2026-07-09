import random

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_product = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            nums_product.append(product)
        return nums_product
    
solution = Solution()

arry1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arry2 = [random.randint(1, 20) for _ in range(10)]
arry3 = [random.randint(1, 20) for _ in range(10)]
arry4 = [random.randint(1, 20) for _ in range(10)]
arry5 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"Array 1:\n{arry1}---", solution.productExceptSelf(arry1))
print(f"Array 2:\n{arry2}---", solution.productExceptSelf(arry2))
print(f"Array 3:\n{arry3}---", solution.productExceptSelf(arry3))
print(f"Array 4:\n{arry4}---", solution.productExceptSelf(arry4))
print(f"Array 5:\n{arry5}---", solution.productExceptSelf(arry5))