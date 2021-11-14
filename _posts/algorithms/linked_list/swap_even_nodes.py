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



def swap_even_nodes(head):
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

    c = head

    next_even=c.next
    if next_even == None:
        return head

    p = c
    while True:

        print("here")
        c=next_even
        n=c.next


        if n is None:
            return head
        else:
            next_even=n.next



        if next_even is None:
            return head

        #Swap
        print(c.value)
        print(next_even.value)

        n.next=c
        c.next=next_even.next

        p.next=next_even
        next_even.next=n


        p=n
        next_even=c
        break;
    return head


a = Node(7)
b = Node(14)
c= Node(21)
d = Node(28)
e = Node(30)

head=a
a.next=b
b.next=c
c.next=d
d.next=e



print_linked_list(head)

print_linked_list(swap_even_nodes(head))

