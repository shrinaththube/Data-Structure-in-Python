'''
Created on Jun 5, 2016

@author: Shrinath Thube
'''
from tree.binarySearchTree import BstOperations,BstExtrafunctions

""" Testing of BstOperations class"""

# Creating tree1 and display it
print "*** --- > Creating Binary search tree1 using createBst method"
tree1 = BstOperations()
test_list1 = [13,8,17,5,10,22,15]
tree1.createBst(test_list1)
tree1.displayTree(tree1.root)

#Create tree2 and try to display without creating
print "*** --- > Creating Binary search tree2 using createBst method"
tree2 = BstOperations()
test_list2 = [10,5,15,20,2,7,13]
tree2.displayTree(tree2.root)
#After creating display
tree2.createBst(test_list2)
tree2.displayTree(tree2.root)


""" Testing of BstExtrafunctions class"""

inLNum = [3,5,10,13,15,18]
preLNum = [10,5,3,15,13,18]
inL = ['D','B','E', 'A','F','C']
preL=['A','B','D','E','C','F']
postL = ['D', 'E', 'B', 'F', 'C', 'A']

#Make tree using inorder and preorder traversal list
print "*** --- > Creating Binary tree1 using inorder and preorder list "
tree3 = BstExtrafunctions()
tree3.root = tree3.createTreeFromInPreOrder(inL,preL,0,len(inL)-1) 
tree3.displayTree(tree3.root)

#Make tree using inorder and postorder traversal list
print "*** --- > Creating Binary tree1 using inorder and postorder list "
tree4 = BstExtrafunctions()
tree4.root = tree4.createTreeFromInPostOrder(inL, postL, 0, len(inL)-1)
tree4.displayTree(tree4.root)

#Make tree using inorder and preorder traversal list
print "*** --- > Creating Binary tree1 using inorder and preorder list "
tree5 = BstExtrafunctions()
tree5.root = tree5.createTreeFromInPreOrder(inLNum,preLNum,0,len(inL)-1) 
tree5.displayTree(tree5.root)
