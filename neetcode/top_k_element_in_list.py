from collections import Counter
from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []

        value = count.most_common(k)
        for key in value:
            print(key[0])
            output.append(key[0])
        return output


if __name__ == "__main__":
    nums = [1, 2, 5, 5, 5, 2, 3, 3, 3]
    k = 2
    solution = Solution()
    solution.topKFrequent(nums=nums, k=k)



