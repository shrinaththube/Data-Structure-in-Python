'''
Created on Jun 8, 2016

@author: Shrinath Thube
'''
class BTNode(object):
    '''
    This is binary tree node contains key, reference to left and right child
    '''
    def __init__(self, key,lChild = None, rChild = None):
        self.key = key
        self.lChild = lChild
        self.rChild = rChild      


class BTOperations(object):
    
    def __init__(self):
        self.root = None
        
    def printInorder(self,refNode):
        if refNode == None: return
        self.printInorder(refNode.lChild)
        print refNode.key,
        self.printInorder(refNode.rChild)
    
    def printPreorder(self,refNode):
        if refNode == None: return
        print refNode.key,
        self.printPreorder(refNode.lChild)
        self.printPreorder(refNode.rChild)
    
    def printPostorder(self,refNode):
        if refNode == None: return
        self.printPostorder(refNode.lChild)
        self.printPostorder(refNode.rChild)
        print refNode.key,
    
    def displayTree(self,refNode):
        if refNode == None:
            print "Tree is not formed yet"
            return
        print
        print "******************* Displaying Tree *********************"
        print "Inorder - ",
        self.printInorder(refNode)
        print
        print "Preorder - ",
        self.printPreorder(refNode)
        print
        print "Postorder - ",
        self.printPostorder(refNode)
        print 
        print "******************* End *********************"
        print
    
    ''' This checks are two tress are mirror to each other Default returns True'''    
    
    def isTreeMirror(self,root1,root2):
        if root1 == None and root2 == None: #recursion breaking condition
            #print "Breaking condition - Both none" # intermediate result for debugging
            return
        if root1 == None or root2 == None: # if one of the root is None then it is not mirror
            #print "False condition - only one is  none", "root1 =", root1,"root2 =", root2 # intermediate result for debugging
            return False
        if root1.key != root2.key : # if keys are different at some depth it is not mirror
            #print "Keys are not equal", root1.key, root2.key # intermediate result for debugging 
            return False
        
        if root1.lChild != None and root1.rChild != None:
            return self.isTreeMirror(root1.lChild, root2.rChild) and self.isTreeMirror(root1.rChild, root2.lChild) 
            
        elif root1.lChild != None:
            return self.isTreeMirror(root1.lChild, root2.rChild)
        
        elif root1.rChild != None:
            return self.isTreeMirror(root1.rChild, root2.lChild)
        
        return True #Default returns true
        
BTree1 = BTOperations()
BTree1.root = BTNode(1)
BTree1.root.lChild = BTNode(3)
BTree1.root.rChild = BTNode(2)
BTree1.root.rChild.lChild = BTNode(5)
BTree1.root.rChild.rChild = BTNode(4)
BTree1.displayTree(BTree1.root)


BTree2 = BTOperations()
BTree2.root = BTNode(1)
BTree2.root.lChild = BTNode(2)
#BTree2.root.rChild = BTNode(3)
BTree2.root.lChild.rChild = BTNode(5)
BTree2.root.lChild.lChild = BTNode(4)
BTree2.displayTree(BTree2.root)

print BTree1.isTreeMirror(BTree1.root, BTree2.root)