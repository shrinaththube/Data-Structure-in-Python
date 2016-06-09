'''
Created on Jun 5, 2016

@author: Shrinath Thube
'''

from tree.binaryTree import BTOperations
from tree.binaryTree import BTNode

class BstOperations(BTOperations):
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
    '''
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
        
        
def main():
    tree1 = BstOperations()
    tree2 = BstOperations()
    tree2.createBst([10,15,7,3,8,13,18])
    tree1.insertNode(10, tree1.root)
    tree1.insertNode(15, tree1.root)
    tree1.insertNode(5, tree1.root)
    tree1.insertNode(20, tree1.root)
    BTOperations.displayTree(tree2, tree2.root)
    BTOperations.displayTree(tree1, tree1.root)
    
    
if __name__ == '__main__':
    main()