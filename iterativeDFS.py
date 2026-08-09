class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    
    #In order
    def inorder(root):
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print(curr.val)
                curr = curr.right
                
                
    #Pre order
    def preorder(root):
        stack = []
        res = []
        curr = root
        
        while curr or stack :
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
                
                
    # Post order
    def postorder(root):
        stack = [root] if root else []
        visit = [False]
        curr = root
        res = []
        
        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    print(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
         