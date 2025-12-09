# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution(object):
#     def inorderTraversal(self, root):
        
        
nodes = [1,None,2,3]
root = TreeNode(nodes[0])
for i in range(1, len(nodes)):
    if i is not None and nodes[i] > root:
        root.right = TreeNode(nodes[i])
    else:
        root.left = TreeNode(nodes[i])

def inorder(node: TreeNode, x):
    if x is not None and x > node.val:
        node.right = TreeNode(x)
    else:
        node.left = TreeNode(x)
        
    return node.left, node.right

