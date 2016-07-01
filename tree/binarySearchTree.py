'''
Created on Jun 5, 2016

@author: Shrinath Thube
'''
from __future__ import division
''' __future__ is a pseudo-module which programmers can use to enable new language features 
which are not compatible with the current interpreter.( -- From stackoverflow)
This is import to make division of two interger as float e.g. 5/10 = 0.5 without this it was 0.
It must imported at beginning of file
'''

from tree.binaryTree import BTOperations
from tree.binaryTree import BTNode
from tree.binaryTree import BTExtraOpeartions


class BstOperations(BTExtraOpeartions):
    '''
    This class contains create bst, display it, insert node
    '''
    def __init__(self):
        self.root = None
    
    def insertNode(self,key,refNode):
        if self.root == None:
            self.root = BTNode(key)
            return
        else:
            if key < refNode.key:
                if refNode.lChild != None:
                    self.insertNode(key,refNode.lChild)
                else:
                    refNode.lChild = BTNode(key)
            else:
                if refNode.rChild != None:
                    self.insertNode(key, refNode.rChild)
                else:
                    refNode.rChild = BTNode(key)
    def createBst(self,list_key):
        if len(list_key) == 0:
            print "List is empty or invalid"
            return 
        for key in list_key:
            self.insertNode(key, self.root)


class BstExtrafunctions(BstOperations):
        
    def __init__(self):
        super(BstExtrafunctions,self).__init__() #it is for using root of the parent
        self.preIndex = 0
        self.postIndex = 0
        
    """ Create tree using inorder traversal list and preorder traversal list. Root is first element in preorder list"""
    def createTreeFromInPreOrder(self,inList,preList,inStart, inLast):
        
        if inStart > inLast or len(preList) == self.preIndex: return None
        
        #print inList, preList
        rEle = preList[self.preIndex]
        self.preIndex +=1
        rootNode = BTNode(rEle)
        
        if inStart == inLast:
            return rootNode
        
        partPoint = inList.index(rEle)
        rootNode.lChild = self.createTreeFromInPreOrder(inList,preList,inStart,partPoint-1)
        rootNode.rChild = self.createTreeFromInPreOrder(inList,preList,partPoint+1,inLast)
        
        return rootNode
    
    """ Create tree using inorder traversal list and postorder traversal list. Root is last element in postorder list"""
    def createTreeFromInPostOrder(self,inList,postList,inStart,inLast):
        
        if inStart > inLast or len(postList)==self.postIndex: return
        
        #Array is scan in reverse order
        rEle = postList[len(postList)-1-self.postIndex]
        self.postIndex +=1
        rootNode = BTNode(rEle)
        
        if inStart == inLast:
            return rootNode
        
        partPoint = inList.index(rEle)
        #Sequence is important First call right subtree then left
        rootNode.rChild = self.createTreeFromInPostOrder(inList, postList, partPoint+1, inLast)
        rootNode.lChild = self.createTreeFromInPostOrder(inList, postList, inStart, partPoint-1)
        
        return rootNode
    
    ''' Returns the sum of min path sum '''
    def findMinSumPathSum(self,refNode):
        if refNode == None:
            #print None, #print for debugging 
            return 0 # recursion breaking condition
        elif refNode.rChild == None:
            """ #print for debugging
            print refNode.key,
            s = self.findMinSumPathSum(refNode.lChild) + refNode.key
            print "returned s- ", s
            return s"""
            return self.findMinSumPathSum(refNode.lChild) + refNode.key
        elif refNode.lChild == None:
            """ #print for debugging
            print refNode.key,
            a = self.findMinSumPathSum(refNode.rChild) + refNode.key
            print "returned a- ", a
            return a"""
            return self.findMinSumPathSum(refNode.rChild) + refNode.key
       
        """ #print for debugging
        print refNode.key,
        t = min(self.findMinSumPathSum(refNode.lChild),self.findMinSumPathSum(refNode.rChild))+refNode.key
        print "returned t - ", t
        return t """
        return min(self.findMinSumPathSum(refNode.lChild),self.findMinSumPathSum(refNode.rChild))+refNode.key
    
    ''' Returns the sum of maximum path sum... Similar as abouve minimum sum path's sum'''
    def findMaxSumPathSum(self,refNode):
        if refNode == None: return 0
        
        elif refNode.rChild == None:
            return self.findMaxSumPathSum(refNode.lChild) + refNode.key
        
        elif refNode.lChild == None:
            return self.findMaxSumPathSum(refNode.rChild) + refNode.key
        
        return max(self.findMinSumPathSum(refNode.lChild),self.findMaxSumPathSum(refNode.rChild)) + refNode.key
    
        
    ''' Returns size ( count of nodes ) of tree
        Number of technics to find size 
        1) Use the following method - count nodes recursively for left subtree and right subtree and add it with root
        2) Traverse tree using any method (In , pre, post order and make one global or instance variable and increment it. 
    '''
    def findSizeOfTree(self,refNode):
        #global size #for second method
        if refNode == None: return 0
        elif refNode.rChild == None:
            return self.findSizeOfTree(refNode.lChild) + 1
        elif refNode.lChild == None:
            return self.findSizeOfTree(refNode.rChild) +1
        #size += 1 # for second method
        #print size, # print debugging for second method
        return self.findSizeOfTree(refNode.lChild) + self.findSizeOfTree(refNode.rChild) +1 
    
    ''' Density = (height of tree/size of tree) 
        1) Can call separate two functions as per following method and calculate density
        2) Can calculate size making size variable global and calculate at calling end
        Advantage of second approach is - do not need to traverse tree twice
    '''
    def findDensityOfTree(self,refNode):
        if refNode == None: return 0
        return (self.findHeightOfTree(refNode)/self.findSizeOfTree(refNode))
    
    '''GeeksforGeeks problem 
        pushing odd keys down towards leaf of tree and making even keys parents
    '''
    def sinkOddNodesInBT(self,refNode):
        if refNode == None: return
        
        if refNode.key % 2 !=0: # this is primary condition to check very important
            if refNode.lChild != None and refNode.lChild.key % 2 == 0:
                temp = refNode.key
                refNode.key = refNode.lChild.key
                refNode.lChild.key = temp
                self.sinkOddNodesInBT(refNode.lChild)
                
            elif refNode.rChild != None and refNode.rChild.key % 2 == 0:
                temp = refNode.key
                refNode.key = refNode.rChild.key
                refNode.rChild.key = temp
                self.sinkOddNodesInBT(refNode.rChild)
        
        self.sinkOddNodesInBT(refNode.lChild)
        self.sinkOddNodesInBT(refNode.rChild)    
    
    
    ''' Finds the root1 Bst contains all nodes as per the root 2 Bst '''
    def areContainsAllNodes(self,root1,root2):
        if root1 == None and root2 == None: return True
        elif root1 != None and root2 == None: return True # Check it for below aswell
        elif root1 == None and root2 != None: return False
        elif root1.key != root2.key: return False
        
        return self.areContainsAllNodes(root1.lChild,root2.lChild) and self.areContainsAllNodes(root1.rChild,root2.rChild) 
    
    ''' Finds the is root2 Bst is sub bst of root1 Bst''' 
    def isItSubBst(self,root1, root2):
        if root1 == None or root2 == None: return False
        refNode1 = root1
        # if roo2 is not present in Bst 1 then refNode will be None at some point and it should check first
        while refNode1 != None and refNode1.key != root2.key:
            if root2.key < refNode1.key:
                refNode1 = refNode1.lChild
            else:
                refNode1 = refNode1.rChild
        return self.areContainsAllNodes(refNode1, root2)   
    
    ''' Checks the nodes is present in Bst or not Time complexity O(log n)'''
    def isNodePresentInBst(self,root,refNode):
        if root == None: return False
        while root != None:
            if root.key == refNode.key: return True
            elif refNode.key < root.key:
                root = root.lChild
            else:
                root = root.rChild
        
        return False
                 
    ''' Find the neareast ancestor in bst '''
    def findLowestCommonAncestor(self,root,refNode1, refNode2):
        if root == None: return None
        # print root.key, refNode1.key, refNode2.key
        if refNode1.key == refNode2.key and refNode2.key == root.key:
            return refNode1
        elif (refNode1.key < root.key and refNode2.key >= root.key)or (refNode1.key >= root.key and refNode2.key < root.key):
            if self.isNodePresentInBst(root, refNode1) and self.isNodePresentInBst(root, refNode2):
                return root
            else: 
                print"Node is not present in tree"
                return None
        elif refNode1.key < root.key and refNode2.key < root.key:
            return self.findLowestCommonAncestor(root.lChild, refNode1, refNode2)
        elif refNode1.key >=  root.key and refNode2.key >=  root.key:
            return self.findLowestCommonAncestor(root.rChild, refNode1, refNode2)
    
    ''' Count the number of nodes from root to desire node '''    
    def numberOfNodesUpToDesireNode(self,root,refNode):
        if root == None: return 0
        elif root.key == refNode.key:
            return 1
        elif root.lChild == None:
            node_count = self.numberOfNodesUpToDesireNode(root.rChild, refNode)
            if node_count == 0: return 0 
            else: return  node_count+ 1
        elif root.rChild == None:
            node_count = self.numberOfNodesUpToDesireNode(root.lChild, refNode)
            if node_count == 0: return 0
            else:  return node_count + 1
        final_count = max( self.numberOfNodesUpToDesireNode(root.lChild, refNode) , self.numberOfNodesUpToDesireNode(root.rChild, refNode) )
        # This is because if the node is not present at all in tree then value should return 0
        if final_count == 0: return 0
        else: return final_count + 1    
    
    ''' Find the minimum distance between two nodes in bst'''  
    def findMinmumDistanceOfTwoNodesInBst(self,root,refNode1,refNode2):
        if root == None: 
            print "Tree is not formed yet"
            return
        lowest_common_ancestor = self.findLowestCommonAncestor(root, refNode1, refNode2) #ancestor will not leaf node in any condition
        # number of nodes at left sides of lowest_common_ancestor + number of nodes at right side + itself
        if lowest_common_ancestor == None: return "One of the node is not in bst "
        return self.numberOfNodesUpToDesireNode(lowest_common_ancestor.lChild, refNode1) + self.numberOfNodesUpToDesireNode(lowest_common_ancestor.rChild, refNode2) + 1  
    
    ''' Does not working..... Finding the bug
    def createFullBinTreeFromPrePostOrder(self,preList,postList,postStart,postLast):
        if postStart > postLast or len(preList) == self.preIndex :
            print "braking condition ", postStart, postLast , postList[postStart:postLast+2], self.postIndex 
            return
        
        print preList, self.preIndex, postList, postStart, postLast, 
        rEle = preList[self.preIndex]
        self.preIndex +=1
        rootNode = BTNode(rEle)
        
        print rootNode.key, postList[postStart:postLast+1],
        

        if postStart == postLast:
            print "return - ", rootNode.key
            return rootNode
        
        partPoint = postList.index(rEle)
        print "part point -" ,partPoint
        
      
        rootNode.lChild = self.createFullBinTreeFromPrePostOrder(preList, postList, postStart, partPoint-1)
        print "start right"
        rootNode.rChild = self.createFullBinTreeFromPrePostOrder(preList, postList, partPoint+1 , postLast)
        
        print "return - ",rootNode.key
        return rootNode
        '''


'''
tree5 = BstExtrafunctions()
preL = [1, 2, 4, 8, 9, 5, 3, 6, 7]
postL = [8, 9, 4, 5, 2, 6, 7, 3, 1]
tree5.root = tree5.createFullBinTreeFromPrePostOrder(preL, postL, 1, len(postL)-2)        
tree5.displayTree(tree5.root)
'''
        
        
class BstNodeAugmented(BTNode):
    
    def __init__(self,key,lNodes=1):
        super(BstNodeAugmented,self).__init__(key)
        self.lNodes = lNodes

class BstAugmented(BstExtrafunctions):
    ''' Find Kth smallest element - This method tkaes
        Time Complexity - O(log h)
        Space - Need to add left node count field while constructing tree''' 
    def findKthSmallestElement(self,root,k):
        if root == None: 
            print root.key
            return
        if k < 1 :
            print "K is not valid - ",k
            return
        
        refNode =  root
        
        while refNode != None:
            if refNode.lNodes == k:
                return refNode
            elif refNode.lNodes > k:
                refNode = refNode.lChild
            else:
                refNode = refNode.rChild
    
        print "K is out of bound"
        return
    
    ''' Increment count of all right side elements if any element added at left side'''
    
    def increamentLNodesValue(self,root):
        if root == None: return
        root.lNodes +=1
        self.increamentLNodesValue(root.lChild)
        self.increamentLNodesValue(root.rChild)
     
    ''' Insert Node in bst with additional left '''
    def insertNode(self, key, root):
        if self.root == None:
            self.root = BstNodeAugmented(key)
        else:
            refNode = root
            newNode = BstNodeAugmented(key)
            while refNode != None:
                if newNode.key < refNode.key:
                    refNode.lNodes += 1
                    self.increamentLNodesValue(refNode.rChild)
                    if refNode.lChild == None:
                        refNode.lChild = newNode
                        return
                    else:
                        refNode = refNode.lChild
                else:
                    newNode.lNodes = refNode.lNodes + 1
                    if refNode.rChild == None:
                        refNode.rChild = newNode
                        return
                    else:
                        refNode = refNode.rChild
    
    def createAugmentedBst(self,elemetnList):
        if len(elemetnList) == 0: 
            print "List is empty"
            return
        for ele in elemetnList:
            self.insertNode(ele, self.root)

        
size =0
def main():
    tree1 = BstOperations()
    tree2 = BstExtrafunctions()
    tree2.createBst([10,15,6,7,3,2,8,9,13,18,19,20])
    tree1.insertNode(10, tree1.root)
    tree1.insertNode(15, tree1.root)
    tree1.insertNode(5, tree1.root)
    tree1.insertNode(20, tree1.root)
    BTOperations.displayTree(tree2, tree2.root)
    BTOperations.displayTree(tree1, tree1.root)
    
    # USe of findMinSumPathSum method
    print "sum = ", tree2.findMinSumPathSum(tree2.root)
    print "Height of tree2 = ", tree2.findHeightOfTree(tree2.root)
    print "size of tree2 = ", tree2.findSizeOfTree(tree2.root)
    print "Density of tree2 = ", tree2.findDensityOfTree(tree2.root)
    #tree2.sinkOddNodesInBT(tree2.root)
    BTOperations.displayTree(tree2, tree2.root) 
    # Serialization 
    serialString = tree2.serializationOfBT(tree2.root)
    #serialString = "10,6,15,3,7,13,18,2,None,None,8,None,None,None,19,None,None,None,None,None,None,None,9,None,None,None,None,None,None,None,20"

    #deserialization
    tree3 = BTExtraOpeartions()
    tree3.root = tree3.deserializationOfBT(serialString)
    BTOperations.displayTree(tree3,tree3.root )
    
    #Test case to check method isItSubBst
    tree4 = BstExtrafunctions()
    bstList4 = [10,5,20,3,8,2,4,7,9,15,25,18,16,21,27,28]
    tree4.createBst(bstList4)
    BTOperations.displayTree(tree4, tree4.root)
    tree5 = BstExtrafunctions()
    bstList5 = [20,15,25,18,21,27]
    tree5.createBst(bstList5)
    BTOperations.displayTree(tree5, tree5.root)
    
    print "tree5 is sub bst of tree4 = ", tree4.isItSubBst(tree4.root, tree5.root) # expected True
    print "tree5 is sub bst of tree1 = ", tree4.isItSubBst(tree1.root, tree5.root) # expected False
    
    #Print boundary elements of tree
    print "All boundary elements - "
    tree4.printBoundaryElementsOfTree(tree4.root)
    
    #finding common lowest ancestor
    print "\n----------------- Finding ancestor---------------------------- \n "
    node1 = BTNode(2)
    node2 = BTNode(9)
    ancestorNode = tree4.findLowestCommonAncestor(tree4.root, node1, node2)
    
    if ancestorNode: print "Lowest common ancestor - ", ancestorNode.key
    
    # find the distance between two nodes in bst
    print "\n--------------distance between two nodes in bst--------------------------------------\n"
    node2.key = 21 
    print "distance - ",tree4.findMinmumDistanceOfTwoNodesInBst(tree4.root, node1, node2)
    
    #find Kth smallest element by augment method. Added one field in node for count of number of leftNodes of each node
    augmentTree1 = BstAugmented()
    augmentTree1.createAugmentedBst([10,15,6,7,3,2,8,9,13,18,19,20])
    
    BTOperations.displayTree(augmentTree1,augmentTree1.root)
    
    print"Kth smallest element = ", augmentTree1.findKthSmallestElement(augmentTree1.root, 10).key
 
    
if __name__ == '__main__':
    #main()
    pass