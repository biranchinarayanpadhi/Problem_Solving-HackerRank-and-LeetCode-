def rev_double_linked_list(head):
    current=head
    ahead=current.next
    current.next=None
    while ahead!=None:
        current.prev=ahead
        temp=ahead.next
        ahead.next=current
        current=ahead
        ahead=temp
    current.prev=None
    head=current
    return head