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


def sort_ll(head):
    '''
    Algo 1:
        1. while:
            Walk the list
                add to a different list at correct position
    :param head:
    :return:
    '''

    sl_h=Node(head.value)
    c1=head.next

    # print(sl_h.value)
    while c1 != None:
        #For each node, set the p, c and add_before
        p=None
        c=sl_h
        add_before=False
        print(c1.value)
        while c != None:
            print(c.value)
            print("----------")

            if c1.value <= c.value:
                add_before=True
                break
            #else walk while keeping track of previous node
            p=c
            c=c.next

        if add_before:
            if p==None:
                n=Node(c1.value)
                n.next=sl_h
                sl_h=n
                # print(sl_h.value)
            else:
                t=p.next
                p.next=Node(c1.value)
                p.next.next=t
        else:
            p.next=Node(c1.value)

        c1=c1.next


    # print(sl_h.value)

    return(sl_h)




a = Node(5)
b = Node(9)
c= Node(10)
d = Node(4)

head=a
a.next=b
b.next=c
c.next=d



#print_linked_list(head)

#r=rev_linked_list(head)
#print_linked_list(r)

#head=del_node(head,14)
#sort_ll(head)
print_linked_list(sort_ll(head))