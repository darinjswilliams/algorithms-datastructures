'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in  O(n)
O(n) time without using the division operation?
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        print(f"Initial output array: {output}")
        
        # Calculate the prefix products
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            print(f"Prefix product at index {i}: {prefix_product}, output: {output}")
            prefix_product *= nums[i]
        
        # Calculate the suffix products and multiply with the prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_product
            print(f"Suffix product at index {i}: {suffix_product}, output: {output}")
            suffix_product *= nums[i]
        
        return output

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    print(result)  # Output: [24, 12, 8, 6]
