# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return head
        if head.next is None:
            return [0]
        dicti={}
        current=head.next
        next_ele=0
        element=0
        stack=[]
        stack.append(head.val)
        res=[]
        dicti={}
        while current:
            
            element=stack.pop()
            
            while element<current.val:
                if element not in dicti:
                    dicti[element]=[current.val]
                    if len(stack)==0:
                        break
                    element=stack.pop()
                else:
                    dicti[element].append(current.val)
                    if len(stack)==0:
                        break
                    element=stack.pop()
                    
            if element>=current.val:
                stack.append(element)
            stack.append(current.val)
            current=current.next
            
        while stack:
            ele=stack.pop()
            if ele not in dicti:
                dicti[ele]=[0]
            else:
                dicti[ele].append(0)
        
        index=0
        temp_index_count={}
        current=head
        while current:
            if current.val not in temp_index_count:
                temp_index_count[current.val]=0
                res.append(dicti[current.val][temp_index_count[current.val]])
            else:
                temp_index_count[current.val]+=1
                res.append(dicti[current.val][temp_index_count[current.val]])
            current=current.next
        return res

           