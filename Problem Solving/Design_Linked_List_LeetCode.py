class Node:
    
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self,val=0,next=None):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.array=[]

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index>=len(self.array):
            return -1
        return self.array[index].val
        
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.array.insert(0,self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node=Node(val)
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        new_node.next=None
        self.array.append(new_node)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index >len(self.array) or index<0:
            return 
        
        new_node=Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            count=0
            current=self.head
            while current:
                if count == index-1:
                    break
                current=current.next
                count+=1
            new_node.next=current.next
            current.next=new_node
        self.array.insert(index,new_node)


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index>=len(self.array) or index<0:
            return -1
        else:
            if index == 0:
                self.head=self.head.next
            else:
                count=0
                current=self.head
                while current:
                    if count == index -1:
                        break
                    current=current.next
                    count+=1
                print(current.val,current.next)
                current.next=current.next.next
            
        self.array.pop(index)
     
 
        
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)