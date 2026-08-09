class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def rev_inorder(root):
    if not root:
        return    
    inorder(root.right)
    print(root.val)
    inorder(root.left)

def rev_preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.right)
    preorder(root.left)

def rev_postorder(root):
    if not root:
        return    
    postorder(root.right)
    postorder(root.left)
    print(root.val)


if __name__ == '__main__':

    root = TreeNode(6)
    root.left = TreeNode(5)
    root.right = TreeNode(8)

    root.left.left = TreeNode(1)
    root.right.right = TreeNode(2)

    root.right.right = TreeNode(19)

print("Inorder:") 
inorder(root) 

print("\nPreorder:") 
preorder(root) 

print("\nPostorder:")
postorder(root)

print("Rev Inorder:") 
rev_inorder(root) 

print("\nRev Preorder:") 
rev_preorder(root) 

print("\nRev Postorder:")
rev_postorder(root)


    