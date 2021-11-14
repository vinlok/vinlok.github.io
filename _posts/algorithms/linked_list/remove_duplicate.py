



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


def remove_duplicate_node(head):
    '''
    Algo:

    walk through the LL
    For each node, see if it is present in a hash table or not.
    If present, then delete it
    else, add to hash

    Deletion logic:

    keep prev_node
    keep current_node

    point prev_node.next to current_node.next
    set current_node to current_node.next


    :param head:
    :return:
    '''

    p=None
    c=head

    hash={}
    while c != None:
        # If the value is present in hash, then skip the node.
        if hash.get(c.value):
            p.next = c.next
        else:
            hash[c.value]=True
            p=c
        c = c.next

    return head


a = Node(7)
b = Node(14)
c= Node(7)
d = Node(28)

head=a
a.next=b
b.next=c
c.next=d


print_linked_list(head)


r=remove_duplicate_node(head)
# print_linked_list(r)

print_linked_list(r)