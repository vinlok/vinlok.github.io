



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

r=rev_linked_list(head)
print_linked_list(r)