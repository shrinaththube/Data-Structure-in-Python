'''
Created on Jun 8, 2016

@author: Shrinath Thube
'''
from _collections import deque
from copy import deepcopy

"""
    ************************* Binary Tree Operations ***************************
    Following problems are covered in this module
    
    1) Inorder traversal - print
    2) Preorder traversal - print
    3) Postorder traversal - print
    4) Level order traversal - print
    5) Reverse Level order traversal ( Bottom to root approach) - print
    6) Spiral Level order traversal (one level from left to right and another from right to left) - print
    7) Print boundary elements of tree
    8) Find if two tress are mirror to each other
    9) Convert tree into it's mirror tree
   10) Create new mirror tree of given tree
   11) Find if two tress are similar to each other
   12) Find node is exist in Binary Tree or not - iterative solution 
   13) Find common ancestor of two nodes in Binary Tree
   14) Count the number of nodes from root to desire node in BT
   15) Serialize the data of binary tree
   16) De-serialize the data to create binary tree 

    ***************************************************************************
""" 



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
    
    ''' Inorder traversal - print  
        Time complexity - O(n) 
        Space complexity - O(1)
    '''        
    def printInorder(self,refNode):
        if refNode == None: return
        self.printInorder(refNode.lChild)
        print refNode.key,
        self.printInorder(refNode.rChild)
   
    ''' Preorder traversal - print  
        Time complexity - O(n) 
        Space complexity - O(1)
    '''        
    def printPreorder(self,refNode):
        if refNode == None: return
        print refNode.key,
        self.printPreorder(refNode.lChild)
        self.printPreorder(refNode.rChild)
   
    ''' Postorder traversal - print  
        Time complexity - O(n) 
        Space complexity - O(1)
    '''        
    def printPostorder(self,refNode):
        if refNode == None: return
        self.printPostorder(refNode.lChild)
        self.printPostorder(refNode.rChild)
        print refNode.key,
    
    ''' Level order traversal - print  
        Print tree in level wise 
        Time complexity - O(n) 
        Space complexity - O(n)
    '''        
    def printLevelOrder(self,refNode):
        if refNode == None: return
        que =  [refNode]
        while len(que)>0:
            temp_que = list()
            for node in que:
                print node.key,
                if node.lChild !=None:
                    temp_que.append(node.lChild)
                if node.rChild != None:
                    temp_que.append(node.rChild)
            print
            que = temp_que

    ''' Reverse Level order traversal ( Bottom to root approach) - print 
        Print level order traversal in reverse manner that is bottom to up approach  
        Time complexity - O(n) 
        Space complexity - O(n)
    ''' 
    def printLevelOrderReverse(self,refNode):
        if refNode == None: return
        print "-----------Reverse level order printing---------"
        st = []
        que =deque()
        que.append(refNode)
        while que:
            node = que.popleft()
            if node.rChild != None:
                que.append(node.rChild)
            if node.lChild != None:
                que.append(node.lChild)
            st.append(node)
        
        while st:
            print st.pop().key,
    
    ''' Spiral Level order traversal (one level from left to right and another from right to left) - print 
        Print level order traversal in reverse manner that is bottom to up approach  
        Time complexity - O(n) 
        Space complexity - O(n)
    ''' 
    def printInSpiralOrder(self,refNode):
        if refNode == None: return
        stL = [] #stack for print left to right nodes
        stR = [] #stack for print right to left nodes
        stR.append(refNode)
        print "-------------Print in spiral order -----------------"
        while stL or stR:
            if stL:
                while stL:
                    node = stL.pop()
                    print node.key,
                    if node.rChild:
                        stR.append(node.rChild)
                    if node.lChild:
                        stR.append(node.lChild)
            else:
                while stR:
                    node = stR.pop()
                    print node.key,
                    if node.lChild:
                        stL.append(node.lChild)
                    if node.rChild:
                        stL.append(node.rChild)
            print ""
        print "------------------End -----------------------"
            
    ''' Print boundary elements of tree  
        Time complexity - O(n) 
        Space complexity - O(n)
    '''        
    def printBoundaryElementsOfTree(self,refNod):
        if refNod == None: 
            print "No tree formed" 
            return
        que = deque()
        que.append(refNod)
        print refNod.key
        while que:
            level_que = deque()
            for node in list(que):
                if node.lChild != None:
                    level_que.append(node.lChild)
                if node.rChild != None:
                    level_que.append(node.rChild)
                if node.lChild == None and node.rChild == None:
                    print node.key,
             
            que = deepcopy(level_que)
            if level_que:
                node = level_que.popleft()
                if node.lChild !=None or node.rChild !=None: print node.key, 
                node = level_que.pop()
                if node.lChild !=None or node.rChild !=None: print node.key 
                
            
    @staticmethod 
    def displayTree(self,refNode): #Static method can be called by class name
        if refNode == None:
            print "Tree is not formed yet"
            return
        print
        print "******************* Displaying Tree *********************"
        print "Level order - ",
        self.printLevelOrder(refNode)
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
    
    
    ''' Find if two tress are mirror to each other 
        This checks are two tress are mirror to each other Default returns True
        Time complexity - O(n) - check every elements in both tree
        Space complexity - O(1)
    '''    
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
    
    ''' Convert tree into it's mirror tree 
        This method make the tree mirror to its original structure
        Time complexity - O(n) - check every elements in both tree
        Space complexity - O(1)
    '''  
    def makeMirrorTree(self,refNode):
        if refNode == None: return # recursion breaking condition
        
        # Swap left and right child from root to leaf
        if refNode.lChild != None and refNode.rChild != None: 
            tempNode = refNode.lChild
            refNode.lChild = refNode.rChild
            refNode.rChild = tempNode
        
        elif refNode.lChild != None:
            refNode.rChild = refNode.lChild
            
        elif refNode.rChild != None:
            refNode.lChild = refNode.rChild
            
        self.makeMirrorTree(refNode.lChild) # recursive call to left subtree
        self.makeMirrorTree(refNode.rChild) # recursive call to right subtree
    
    ''' Create new mirror tree of given tree 
        This will construct new mirror tree without changing original tree
        Time complexity - O(n) - check every elements in both tree
        Space complexity - O(1)
    '''  
    def createNewMirrorTree(self,refNode):
        if refNode == None: return # breaking condition of recursion
        
        rootNode = BTNode(refNode.key) # create new binary tree node
        
        if refNode.lChild == None and refNode.rChild == None: #return leaf node - breaking condition
            return rootNode
        
        rootNode.lChild = self.createNewMirrorTree(refNode.rChild) #recursive call
        rootNode.rChild = self.createNewMirrorTree(refNode.lChild) #recursive call
        
        return rootNode #returns root of new tree

    ''' Find if two tress are similar to each other 
        Check are two trees similar or not - Default returns true
        Time complexity - O(n) - check every elements in both tree
        Space complexity - O(1)
    '''    
    def areTwoTreeSimilar(self,root1,root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.key != root2.key: return False
        return self.areTwoTreeSimilar(root1.lChild, root2.lChild) and self.areTwoTreeSimilar(root1.rChild, root2.rChild) 
 
    ''' Find height of tree 
        Returns height or depth of tree - longest path between root and leaf
        Time complexity - O(log h) - calculate for left sub tree and right sub tree
        Space complexity - O(1)
    '''    
    def findHeightOfTree(self,refNode):
        if refNode == None: return 0
        elif refNode.lChild == None:
            return self.findHeightOfTree(refNode.rChild) + 1
        elif refNode.rChild == None:
            return self.findHeightOfTree(refNode.lChild) + 1
        return max(self.findHeightOfTree(refNode.lChild),self.findHeightOfTree(refNode.rChild))+1

    
    ''' Find common ancestor of two nodes in Binary Tree 
        Returns ancestor node 
        Time complexity - O(n) 
        Space complexity - O(1)
    '''
    # This function handles edge case of if any node is not present in BT
    def findCommonAncestorinBT(self,root,node1,node2):
        if root == None: return None
        if not self.isNodePresentInBT(root, node1): 
            print "Node is not present - ", node1.key
            return None
        if not self.isNodePresentInBT(root, node2): 
            print "Node is not present - ", node2.key
            return None
        return self.RecursionfindCommonAncestor(root, node1, node2)

    # This is main function that find lowest common ancestor of two nodes 
    def RecursionfindCommonAncestor(self,root,node1,node2):
        if root == None: return None
        if root.key == node1.key or root.key == node2.key: return root.key
        if root.lChild == None and root.rChild == None: return None
        
        firstNode = self.RecursionfindCommonAncestor(root.lChild, node1, node2)
        secondNode = self.RecursionfindCommonAncestor(root.rChild, node1, node2)
        
        if firstNode and secondNode: return root.key
        
        if firstNode: return firstNode
        if secondNode: return secondNode
        
        return None
    
    ''' Find node is exist in Binary Tree or not - iterative solution 
        Returns True or False
        Time complexity - O(n) 
        Space complexity - O(n)
    '''
    def isNodePresentInBT(self,root,refNode):
        if root == None: return False
        que = deque()
        que.append(root)
        while que:
            node =que.popleft()
            if node.key == refNode.key: return True
            if node.lChild: que.append(node.lChild)
            if node.rChild: que.append(node.rChild)
        return False
    
    ''' Count the number of nodes from root to desire node in BT
        Time complexity - O(n) Need to find node in BT so need to scan all elements
        Space complexity - O(1)
    '''    
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
    

class BTExtraOpeartions(BTOperations):
    
    '''  Serialize the data of binary tree 
        LeetCodeProblem 
        serialize all nodes keys in string and send to server. It sends all keys as well as None 
        Returns height or depth of tree - longest path between root and leaf
        Time complexity - O(n) 
        Space complexity - O(n)
    '''    
    def serializationOfBT(self,refNode):
        if refNode == None: return
        height = self.findHeightOfTree(refNode)
        maxSizeOfTree = 2**height
        serialList = list()
        que = deque([refNode])
        serialList.append(str(refNode.key))
        while que:
            if len(serialList) >= maxSizeOfTree-1:
                break
            temp = que.popleft()
            if temp:
                if temp.lChild != None:
                    serialList.append(str(temp.lChild.key))
                else: serialList.append("None")
                
                if temp.rChild != None: 
                    serialList.append(str(temp.rChild.key))
                else: serialList.append("None")
                que.append(temp.lChild)
                que.append(temp.rChild)
            else:
                que.append(temp)
                que.append(temp)
                serialList.append("None")
                serialList.append("None")
                
        return (",").join(serialList)   
    
      
    
    '''  De-serialize the data to create binary tree 
        LeetCodeProblem 
        Try to make receiver as simple as possible. Server should be simple 
        Returns height or depth of tree - longest path between root and leaf
        Time complexity - O(n) 
        Space complexity - O(n)
    '''    
    def deserializationOfBT(self,keys):
        if len(keys) == 0 :return None
        keys = deque(keys.split(","))
        key = keys.popleft()
        root = None
        if key != "None":
            root = BTNode(int(key))
        que = deque([root])
        while que and len(keys) >0:
            temp = que.popleft()
            left = keys.popleft()
            right = keys.popleft()
            if temp != None:
                temp.lChild = BTNode(int(left)) if left != "None" else None
                temp.rChild = BTNode(int(right)) if right != "None" else None
                que.append(temp.lChild)
                que.append(temp.rChild)
      
        return root
        
def main():
    
    BTree1 = BTOperations()
    BTree1.root = BTNode(1)
    BTree1.root.lChild = BTNode(3)
    BTree1.root.rChild = BTNode(2)
    BTree1.root.rChild.lChild = BTNode(5)
    BTree1.root.rChild.rChild = BTNode(4)
    print"BTree1 -"
    BTree1.displayTree(BTree1,BTree1.root)
    
    BTree2 = BTOperations()
    BTree2.root = BTNode(1)
    BTree2.root.lChild = BTNode(2)
    BTree2.root.rChild = BTNode(3)
    BTree2.root.lChild.rChild = BTNode(5)
    BTree2.root.lChild.lChild = BTNode(4)
    print"BTree2 -"
    BTree2.displayTree(BTree2,BTree2.root)
    
    print"BTree1 is mirror of BTree2 - ", BTree1.isTreeMirror(BTree1.root, BTree2.root)
    
    print "Making BTree1 to its mirror - SO BTree1 = BTree2"
    
    #BTree1.makeMirrorTree(BTree1.root)
    
    BTree1.displayTree(BTree1,BTree1.root)
    
    ''' Construct BTree3 as a mirror of BTree1'''
    print "Construct BTree3 as a mirror of BTree1"
    BTree3 = BTOperations()
    BTree3.root = BTree3.createNewMirrorTree(BTree1.root)
    print"BTree3 -"
    BTree3.displayTree(BTree3,BTree3.root)
    
    
    ''' Checking trees are similar'''
    
    print "Are this trees similar - " ,BTree3.areTwoTreeSimilar(BTree1.root,BTree1.root)
    print "Are this trees similar - " ,BTree3.areTwoTreeSimilar(BTree3.root,BTree1.root)
    
    BTree3.printLevelOrder(BTree3.root)
    

if __name__ == '__main__':
    main()