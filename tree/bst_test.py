'''
Created on Jun 5, 2016

@author: Shrinath Thube
'''
from tree.binarySearchTree import BstOperations

# Creating tree1 and display it
tree1 = BstOperations()
test_list1 = [13,8,17,5,10,22,15]
tree1.createBst(test_list1)
tree1.displayTree(tree1.root)

#Create tree2 and try to display without creating
tree2 = BstOperations()
test_list2 = [10,5,15,20,2,7,13]
tree2.displayTree(tree2.root)
#After creating display
tree2.createBst(test_list2)
tree2.displayTree(tree2.root)