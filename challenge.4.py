# Number of Visible Nodes
# There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
# Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
# Signature int visibleNodes(Node root) {
# InputThe root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000
# OutputAn int representing the number of visible nodes.
# Example
# 8  <------ root
#            / \
#          3    10
#         / \     \
#        1   6     14
#           / \    /
#          4   7  13
# output = 4

class Node(object):

    def addValue(self, value):
        if not hasattr(self, 'value'):
            self.value = value
            return

        if self.value > value:
            if not hasattr(self, 'left'):
                self.left = Node()

            self.left.addValue(value)
        else:
            if not hasattr(self, 'right'):
                self.right = Node()

            self.right.addValue(value)

def maxDepth(node):

    if node == None:
        return 0

    maxLeft = maxRight = 0
    if hasattr(node, 'left'):
        maxLeft = maxDepth(node.left)
    
    if hasattr(node, 'right'):
        maxRight = maxDepth(node.right)

    if maxLeft > maxRight:
        return maxLeft + 1
    
    return maxRight + 1

def visibleNodes(root):
    return maxDepth(root)

root = Node()

root.addValue(8)
root.addValue(3)
root.addValue(10)
root.addValue(1)
root.addValue(6)
root.addValue(14)
root.addValue(4)
root.addValue(7)
root.addValue(13)

print(visibleNodes(root))