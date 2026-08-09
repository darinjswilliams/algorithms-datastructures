


class Kandanes: 
   # Brute Force: O(n^2)
    def bruteForce(self, nums):
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        return maxSum

    # Kadane's Algorithm: O(n)
    def kadanes(self, nums):
        """ 
        Compute the maximum subarray sum using Kadane's Algorithm.

        The algorithm maintains a running sum that resets when it becomes counterproductive (negative), 
        ensuring O(n) time and O(1) space. 

        Parameters ---------- 
            nums : List[int] A list of integers (positive, zero, or negative).
        Returns -------
            int The maximum sum of any contiguous subarray.
         """
        maxSum = nums[0]
        curSum = nums[0]

        for n in nums[1:]:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
        return maxSum

    # Return the left and right index of the max subarray sum,
    # assuming there's exactly one result (no ties).
    # Sliding window variation of Kadane's: O(n)
    def slidingWindow(self, nums):
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R

            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R 

        return [maxL, maxR]
    
if __name__ == "__main__":
    from typing import List

    kalg = Kandanes()
    mlst:List = [1, 4, 5,6,7,-3,4,8]

    print(kalg.kadanes(mlst))
