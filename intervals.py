from typing import List

class TimeOverlap:

    def eraseOverLapIntervals(self, intervals: List[List[int]]) -> int:
        
        if 0 <= len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[1])
    
        
        removed = 0
        last_end = intervals[0][1]
        
        for r in range(1, len(intervals)):
            if intervals[r][0] >= last_end:
                last_end = intervals[r][1]
            else:
                removed += 1
                
        return removed

import timeit

intervals = [[1,2],[3,5],[9,10]]
new_interval = [6,7]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #base case
        if len(intervals) == 0:
            return [newInterval]

        result = []
        i = 0
        n = len(intervals)

        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
                        
        return result
    
    
    def insert2(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # 1. Add intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # 3. Add the remaining intervals
        result.extend(intervals[i:])

        return result
    
    def baseTest(self):

        ITER = 1_000_000

        tests = {
            "insert method 1": "self.insert(intervals, new_interval)",
            "insert method 2 ": "self.insert2(intervals, new_interval)",
        }

        # IMPORTANT: No indentation inside this string
        setup = """
from __main__ import intervals, new_interval, insertTest
self = insertTest
"""

        print(f"Benchmarking with Intervala={intervals} for {ITER:,} iterations: with K value: {new_interval}\n")
        print(f"{'Method':20s} | {'Result':6s} | Time (seconds)")
        print("-" * 50)

        for name, stmt in tests.items():
            result = eval(stmt)
            t = timeit.timeit(stmt, setup=setup, number=ITER)
            print(f"{name:20s} | {str(result):6s} | {t:.6f}")


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #base case
        if len(intervals) == 0:
            return intervals

        
        results = []

        #sort intervals in place
        intervals.sort(key=lambda x: x[0])
        
        #get first interval
        current_interval = intervals[0]
        results.append(current_interval)

        #start interval at 1
        for i in range(1, len(intervals)):
            #set next interval to intervals at position 1
            next_interval = intervals[i]
            
            # check for overlap, if so than we get the max from the end time
            if next_interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                # set the current interval to the next interval
                current_interval = next_interval
                results.append(current_interval)
                

        return results
    
    
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #base case
        if len(intervals) == 0:
            return intervals
        
        results = []
        
        #sort in place
        intervals.sort(key=lambda x: x[0])
        
        current_interval = intervals[0]   # get first interval
        results.append(current_interval)   #append the first interval in list
        
        N = len(intervals)
        
        for i in range(1, N ):
            
            if intervals[i][0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                current_interval = intervals[i]
                results.append(current_interval)
        
        return results
        


if __name__ == "__main__":
    
    # overLap = TimeOverlap()
    # myList = [[1,2], [2,4], [1,4]]
    
    # print(overLap.eraseOverLapIntervals(myList))      #1
    # print(overLap.eraseOverLapIntervals([[1,2],[2,4]])) #0
    
    insertTest = Solution()
    print(insertTest.baseTest())
    
    m_interval =MergeIntervals()
    
    print("-" * 30)
    print("Merged Interval")
    print(m_interval.merge([[1,3],[1,5],[6,7]]))
    print(m_interval.merge2([[1,3],[1,5],[6,7]]))
    
    
    