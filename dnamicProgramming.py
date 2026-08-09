class UnboundKnapSack:
    
    """
        Brute force 
        Time O(2^n)
        Space O(m)

    """
    def dfs(self, profit, weight, capacity):
        return self.dfsHelper(0, profit, weight, capacity)
                
                
    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0
            
        
        #skip, when your skip your adding 1 to it, so i+1    
        maxProfit = self.dfsHelper(i+1, profit, weight, capacity)
        
        #include item i, create a new capacity
        newCap = capacity - weight[i]
        
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i, profit, weight, newCap)
            
            # compute the max
            maxProfit = max(maxProfit, i)
            
        return maxProfit
        

class Memorization:
    # Memoization Solution
    # Time: O(n * m), Space: O(n * m)
    # Where n is the number of items & m is the capacity.
    
    def memorization(self, profit, weight, capacity):
         
        N, M = len(profit), capacity
         
        cache = [[-1] * (M + 1) for _ in range(N)]
        
        return self.helper(0, profit, weight, capacity, cache)
    
    def helper(self, i, profit, weight, capacity, cache):
        
        
        if i == len(profit):
            return 0
        
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        #skip item i
        cache[i][capacity] = self.helper(i+1, profit, weight, capacity, cache)
        
        # get new capacity
        newCap = capacity - weight[i]
        
        if newCap >= 0:
            # add item, if this is the 0/1 knapsack you add i + 1
            p = profit[i] + self.helper(i, profit, weight, capacity, cache)
            
            # compute the max profit and add to cache, with unbound you can keep on adding
            capacity[i][capacity] = max(p, cache[i][capacity])
            
        return cache[i][capacity]
            
        
        
        
class LCS:
    """Longest Common SubSequence """
    def dfs(self, s1, s2):
        """
            Timne: O(2^(n+m))
            Space: O(n+m)
            
            Recusion Solution
        """
        N, M = len(s1), len(s2)
        cache = [[-1] * (M) for _ in range(N)]
        
        return self.dfsHelper(s1, s2, 0, 0, cache)
    
    def dfsHelper(self, s1, s2, i1, i2, cache):
        
        #base case if one of the indexs go out of bounds
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        # check cache if we have already computed the longest common subsequence for these indexs
        if cache[i1][i2] != -1:
            return cache[i1][i2]
        
        # if the sub seq are a match return 1
        if s1[i1] == s2[i2]:
            cache[i1][i2] = 1 + self.helper(s1, s2, i1+1, i2+1, cache)
        else:
        # increate indexs by 1 and return the max
            cache[i1][i2] = max(self.dsHelper(s1, s2, i1+1, i2, cache), 
                       self.dfsHelper(s1, s2, i1, i2+1, cache))
        return cache[i1][i2]
            
            
    def dp(self, s1, s2):
        """
        Time O(n*m)
        Space O(n+m)
        
        """
        N, M = len(s2), len(s1) 
        dp = [[0] * (M+1) for _ in range(N+1)]
        
        for i in range(N):
            for j in range(M):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = 1 +dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[N][M]
        
        
    def optimizedDp(self, s1, s2):
        """
        Tine O(n * m)
        space O(m)
        """
        
        N, M = len(s1), len(s2)
        dp = [0] * (M+1)
        
        for i in range(N):
            curRow = [0] * (M+1)
            
            for j in range(M):
                if s1[i] == s2[j]:
                    curRow[j+1] = 1 + dp[j]
                else:
                    curRow[j+1] = max(dp[j+1], curRow[j])
                    
            dp = curRow
            
        return dp[M]
        
        
        
        
        
        