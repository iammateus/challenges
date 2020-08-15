# Print a binary tree
# 
# 8  <------ root
#            / \
#          3    10
#         / \     \
#        1   6     14
#           / \    /
#          4   7  13
# output = 4

from math import pow
from math import ceil

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
    
    def byDepth(self, wanted, depth = -1):
        depth += 1

        if depth == wanted:
            return [ self.value ]
        
        result = []
        if hasattr(self, 'left'):
            result = result + self.left.byDepth(wanted, depth)
        else:
            diff = 1

            if wanted - depth > 1:
                diff = int(pow(2, wanted - depth - 1))

            for count in range(diff):
                result = result + [ ' ' ]
        
        if hasattr(self, 'right'):
            result = result + self.right.byDepth(wanted, depth)
        else:
            diff = 1

            if wanted - depth > 1:
                diff = int (pow(2, wanted - depth - 1))
            
            for count in range(diff):
                result = result + [ ' ' ]

        return result

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

def printTree(root):
    depth = maxDepth(root)
    chars = len(root.byDepth(depth))

    for count in range(depth):
        numberOfNodes = int(pow(2, count))
        spaces = chars // numberOfNodes 
        
        values = root.byDepth(count)

        result = ""
        for countVal in range(len(values)):
            value = values[countVal]

            if not (count == depth and countVal == len(values) - 1):
                result += str(value).center(spaces, " ")
         
        
        print("|" + result + "|")
        
        if(count == depth -1):
            return 

        spaces = chars // (numberOfNodes * 2) 
        nextVals = root.byDepth(count + 1)
        
        result = ""
        for countVal in range(len(values)):
            index = countVal + 1

            if index == 1:
                indexLeft = 0
                indexRight = 1
            else:
                indexLeft = index * 2 - 2
                indexRight = index * 2 - 1
            

            if(nextVals[indexLeft] != " "):
                result += '/'.rjust(spaces // 2).center(spaces, " ")
            else:
                result += ' '.center(spaces, " ")

            if(nextVals[indexRight] != " "):
                result += '\\'.ljust(spaces // 2).center(spaces, " ")
            else:
                result += ' '.center(spaces, " ")

        print("|" + result + "|")

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
root.addValue(15)
root.addValue(17)
root.addValue(20)

printTree(root)