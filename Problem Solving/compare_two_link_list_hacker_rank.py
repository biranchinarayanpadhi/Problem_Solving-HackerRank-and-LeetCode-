def compare_lists(llist1, llist2):
    count=0
    count1=0

    head=llist1
    head1=llist2

    if head!=None:
        current=head
        while current!=None:
            count+=1
            current=current.next
    
    if head1!=None:
        current=head1
        while current!=None:
            count1+=1
            current=current.next
    
    if count1 == count:
        current1=head
        current2=head1
        while current1!=None and current2!=None:
            if current1.data==current2.data:
                current1=current1.next
                current2=current2.next
            else:
                return 0
    else:
        return 0
    
    return 1