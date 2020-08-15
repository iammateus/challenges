# Being given a list of binary trees print all nodes that have the same position and the same value in all trees:
# 
# Signature array printEqualNodes(array [ Node nodes ]) {
# Input the array of root nodes
# Output the values which exist in all trees in the same position.
# 
# Example
# Input:
# 
# First tree
# 10  <------ root
#            / \
#          9    11
#                 \
#                  12
#                    \
#                     15
# 
# Second tree
# 10  <------ root
#            / \
#          9    11
#         /       \
#        6         12
#                    \
#                     14
# 
# Output:
# 10, 9, 11, 12

class Node(object):

    def __init__(self, value):
        self.value = value
    
    def addValue(self, value):
        if not hasattr(self, 'value'):
            self.value = value
            return

        if self.value > value:
            if not hasattr(self, 'left'):
                self.left = Node(value)
            else:
                self.left.addValue(value)
        else:
            if not hasattr(self, 'right'):
                self.right = Node(value)
            else:
                self.right.addValue(value)

    def __str__(self):
        return str(self.value)

def printEqualNodes(nodes):

    if len(nodes) == 0: 
        return []

    result = []

    isEquals = True
    for count in range(len(nodes)):
        # print(nodes[count].value)
        if count != 0 and nodes[count - 1].value !=  nodes[count].value:
            isEquals = False
    
    if isEquals:
        result.append(nodes[0].value)

    leftNodes = []
    rightNodes = []

    for count in range(len(nodes)):
        if hasattr(nodes[count], 'left'):
             leftNodes.append(nodes[count].left) 
        
        if hasattr(nodes[count], 'right'):
             rightNodes.append(nodes[count].right) 
        

    if len(leftNodes) == len(nodes):
        result = result + printEqualNodes(leftNodes)
    
    if len(rightNodes) == len(nodes):
        result = result + printEqualNodes(rightNodes)

    return result



tree1 = Node(10)
tree1.addValue(9)
tree1.addValue(11)
tree1.addValue(12)
tree1.addValue(15)

tree2 = Node(10)
tree2.addValue(9)
tree2.addValue(6)
tree2.addValue(11)
tree2.addValue(12)
tree2.addValue(14)

print(str(printEqualNodes([ tree1, tree2 ])))