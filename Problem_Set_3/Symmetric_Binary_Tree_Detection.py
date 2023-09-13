class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def isMirror(left_subtree, right_subtree):
    if left_subtree is None and right_subtree is None:
        return True
    
    if left_subtree is None or right_subtree is None:
        return False
    
    return (left_subtree.value == right_subtree.value) and \
            isMirror(left_subtree.left, right_subtree.right) and \
            isMirror(left_subtree.left, right_subtree.right)

def isSymmetric(root):
    if root is None:
        return True
    
    return isMirror(root.left, root.right)
    
if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    
    root3 = TreeNode(1)

    result = list(map(isSymmetric, [root1, root2, root3]))
    print(result)