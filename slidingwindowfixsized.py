import timeit
from typing import List

NUM: List = [1, 2, 34, 34, 3, 2, 2, 2, 8]
k = 2

class SlidingWindowFixedSize:
    # Check if array contains a pair of duplicate values,
    # where the two duplicates are no farther than k positions from 
    # each other (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
    # O(n * k)
    def closeDuplicatesBruteForce(self, nums, k):
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k)):
                if nums[L] == nums[R]:
                    return True
        return False

    # Same problem using sliding window.
    # O(n)
    def closeDuplicates(self, nums, k):
        window = set()  # Current window of size <= k
        L = 0

        for R in range(len(nums)):
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

    def closeDuplicatesSimple(self, nums, k):
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            # Keep window size <= k
            if i >= k:
                window.remove(nums[i - k])

        return False

    def baseTest(self):

        ITER = 1_000_000

        tests = {
            "simple method": "self.closeDuplicatesSimple(NUM, k)",
            "track window": "self.closeDuplicates(NUM, k)",
            "brute": "self.closeDuplicatesBruteForce(NUM, k)",
        }

        # IMPORTANT: No indentation inside this string
        setup = """
from __main__ import sw, NUM, k
self = sw
"""

        print(f"Benchmarking with NUM={NUM} for {ITER:,} iterations: with K value: {k}\n")
        print(f"{'Method':20s} | {'Result':6s} | Time (seconds)")
        print("-" * 50)

        for name, stmt in tests.items():
            result = eval(stmt)
            t = timeit.timeit(stmt, setup=setup, number=ITER)
            print(f"{name:20s} | {str(result):6s} | {t:.6f}")


if __name__ == '__main__':
    sw = SlidingWindowFixedSize()
    print(sw.baseTest())
