'''
Created on Jul 23, 2016

@author: Shrinath Thube
'''

class LLNode(object):
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LLOperations(object):
    
    def __init__(self):
        self.head = None
    
    def creatLL(self,arr):
        for ele in arr:
            if self.head == None: 
                self.head = LLNode(arr[0])
                trav = self.head
            else:
                trav.next = LLNode(ele)
                trav = trav.next
                
    def displayLL(self,head):
        if head == None: return
        trav = head
        while trav !=None:
            print trav.data, "-->",
            trav = trav.next
            
        print "None" 
            
    def insertNodeAtEnd(self,data):
        if self.head == None:
            self.head = LLNode(data)
        
        trav = self.head
        while trav.next !=None:
            trav = trav.next
        
        trav.next = LLNode(data)
        
    def insertNodeAtHead(self,data):
        if self.head == None:
            self.head = LLNode(data)
        
        newNode = LLNode(data)
        newNode.next = self.head
        self.head = newNode
            

list1 = LLOperations()
arr1 = [3,5,1,6,2,7,8,4]
list1.creatLL(arr1)
list1.displayLL(list1.head)
list1.insertNodeAtEnd(9)
list1.displayLL(list1.head)
list1.insertNodeAtHead(10)
list1.displayLL(list1.head)
        
    
