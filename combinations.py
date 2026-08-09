def findCombinationsByWeightIndices(weights, capacity):
    # Write your code here
    res = []
    
    def helper(i, curCombs, total):
            
        if total == capacity:
            res.append(curCombs.copy())
            return
            
        #check out of bounds
        if i >= len(weights) or total > capacity:
            return
            
        curCombs.append(i)
        helper(i, curCombs, total + weights[i])
        curCombs.pop()
        
        #exclude
        helper(i+1, curCombs, total)
        
    helper(0, [], 0)
    return res

if __name__ == "__main__":
    weights = [2, 3, 5]
    capacity = 5
    print(findCombinationsByWeightIndices(weights, capacity))