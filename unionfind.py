class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
        
    #find parent of n, with path compression.
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    #union by height / rank
    # Return false if already connected, true otherwise
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1  
        
        return True
    
    
if __name__ =="__main__":
    uf = UnionFind(5)
    print(uf.union(1, 2))  # True
    print(uf.union(2, 3))  # True
    print(uf.union(1, 3))  # False (already connected)
    print(uf.find(1))       # Should return the representative of the set containing 1
    print(uf.find(2))       # Should return the same representative as find(1)
    print(uf.find(3))       # Should return the same representative as find(1) and find(2)
    print(uf.union(4, 5))  # True
    print(uf.union(3, 4))  # True (connects the two sets)
    
            