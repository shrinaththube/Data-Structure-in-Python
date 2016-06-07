'''
Created on Jun 5, 2016

@author: Shrinath Thube
'''

class BstNode(object):
    '''
    This is bst node contains key, reference to left and right child
    '''
    def __init__(self, key,lChild = None, rChild = None):
        self.key = key
        self.lChild = lChild
        self.rChild = rChild      


class BstOperations(object):
    '''
    This class contains create bst, display it, insert node
    '''
    def __init__(self):
        self.root = None
    
    def insertNode(self,key,refNode):
        if self.root == None:
            self.root = BstNode(key)
            return
        else:
            if key < refNode.key:
                if refNode.lChild != None:
                    self.insertNode(key,refNode.lChild)
                else:
                    refNode.lChild = BstNode(key)
            else:
                if refNode.rChild != None:
                    self.insertNode(key, refNode.rChild)
                else:
                    refNode.rChild = BstNode(key)
    
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
        rootNode = BstNode(rEle)
        
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
        rootNode = BstNode(rEle)
        
        if inStart == inLast:
            return rootNode
        
        partPoint = inList.index(rEle)
        #Sequence is important First call right subtree then left
        rootNode.rChild = self.createTreeFromInPostOrder(inList, postList, partPoint+1, inLast)
        rootNode.lChild = self.createTreeFromInPostOrder(inList, postList, inStart, partPoint-1)
        
        return rootNode

def main():
    tree1 = BstOperations()
    tree2 = BstOperations()
    tree2.createBst([10,15,7,3,8,13,18])
    tree1.insertNode(10, tree1.root)
    tree1.insertNode(15, tree1.root)
    tree1.insertNode(5, tree1.root)
    tree1.insertNode(20, tree1.root)
    tree2.displayTree(tree2.root)
    tree1.displayTree(tree1.root)
    
if __name__ == '__main__':
    main()