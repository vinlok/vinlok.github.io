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



def swap_head_with_nth(head,n):

    '''
     Algo:
     1. Start with p=None, c=head and n_node=c.next.
     2. walk c pointer n steps:
        first, set a counter i to 1 (as you are on the first node)



        now untill i is at n
            set p=c
            move c by 1 step
            move n_node to c.next

        now swap cth node with the head node
            point temp to head->next

            point p-next to head
            point head-next to c-next
            then point head to c
            c-next to temp
    '''

    p=None
    c=head
    n_node=c.next

    i = 1

    # Walk upto nth node
    while i != n+1:
        p=c
        c=c.next
        n_node=c.next
        i += 1
        if n_node==None and i != n+1:
            return False

    temp= head.next
    p.next=head
    head.next=c.next
    head=c
    c.next=temp

    return(head)

a = Node(7)
b = Node(14)
c= Node(21)
d = Node(28)

head=a
a.next=b
b.next=c
c.next=d


print_linked_list(head)




n_l=swap_head_with_nth(head,2)
print_linked_list(n_l)