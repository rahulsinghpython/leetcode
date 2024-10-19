# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in
# O
# (
# n
# )
# O(n) time without using the division operation?

from collections import Counter
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for item in nums:
            new_nums = nums.copy()
            new_nums.remove(item)
            products.append(Solution.multiply(new_nums))
        return products

    def multiply(nums: List[int]):
        value = 1
        for num in nums:
            value *= num
        return value


if __name__ == "__main__":
    solution = Solution()

    solution.productExceptSelf([1, 2, 4, 6])
