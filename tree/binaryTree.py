'''
Created on Jun 8, 2016

@author: Shrinath Thube
'''
from _collections import deque
from test._mock_backport import right
from copy import deepcopy

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
     
    ''' Print tree in level wise '''   
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
    
    ''' This method make the tree mirror to its original structure '''
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
    
    ''' This will construct new mirror tree without changing original tree'''
    def createNewMirrorTree(self,refNode):
        if refNode == None: return # breaking condition of recursion
        
        rootNode = BTNode(refNode.key) # create new binary tree node
        
        if refNode.lChild == None and refNode.rChild == None: #return leaf node - breaking condition
            return rootNode
        
        rootNode.lChild = self.createNewMirrorTree(refNode.rChild) #recursive call
        rootNode.rChild = self.createNewMirrorTree(refNode.lChild) #recursive call
        
        return rootNode #returns root of new tree
    
    ''' Check are two trees similar or not - Default returns true'''
    def areTwoTreeSimilar(self,root1,root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.key != root2.key: return False
        return self.areTwoTreeSimilar(root1.lChild, root2.lChild) and self.areTwoTreeSimilar(root1.rChild, root2.rChild) 
    
    ''' Returns height or depth of tree - longest path between root and leaf'''
    def findHeightOfTree(self,refNode):
        if refNode == None: return 0
        elif refNode.lChild == None:
            return self.findHeightOfTree(refNode.rChild) + 1
        elif refNode.rChild == None:
            return self.findHeightOfTree(refNode.lChild) + 1
        return max(self.findHeightOfTree(refNode.lChild),self.findHeightOfTree(refNode.rChild))+1


class BTExtraOpeartions(BTOperations):
    
    ''' LeetCodeProblem 
    serialize all nodes keys in string and send to server. It sends all keys as well as None'''
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
    
    
    
    ''' LeetCodeProblem 
    Try to make reciever as simple as possible. Server should be simple'''    
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