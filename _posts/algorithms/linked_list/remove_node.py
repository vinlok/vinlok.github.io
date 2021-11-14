class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None




def print_linked_list(head):
    cur_node=head
    while cur_node != None:
        print(cur_node.value)
        cur_node=cur_node.next



def del_node(head,entry):
    '''
    :param head:
    :return:

    head->7->14->21->28->None


    Algo:

    1. Start with p=None and c=head
    2. Go while (c != None):
        If current node value is matching with what needs to be deleted
            then
             if not p: //p is not none
                p.next=c.next
             else
                 head=c.next
                break

        p=c
        c=c.next



    '''


    p=None
    c=head

    while c != None:
        if c.value==entry:
            if p != None:
                p.next=c.next
                print("deleted")
            else:
                head=c.next
            break;
        p=c
        c=c.next

    return(head)



def rev_linked_list(head):
    '''
    Algo:
    head->7->14->21->28->None
    None                 head

    set cur_node to head

    while cur_node !=  None:

    t = cur_node.next
    t.prev_node=cur_node
    cur_node.next= None
    cur_node= t

    :param head:
    :return:
    '''

    cur_node = head
    t1 = cur_node.next
    cur_node.next=None
    while t1 != None:
        t = t1
        t1=t.next
        t.next = cur_node
        cur_node = t

    return(cur_node)
a = Node(7)
b = Node(14)
c= Node(21)
d = Node(28)

head=a
a.next=b
b.next=c
c.next=d



print_linked_list(head)

#r=rev_linked_list(head)
#print_linked_list(r)

head=del_node(head,14)
print_linked_list(head)