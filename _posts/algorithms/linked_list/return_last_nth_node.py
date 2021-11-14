



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


def return_last_nth_node(head,n):
    '''
    Use the runner technique.
    Algo:
    1. set r and c to head.
    2. now while r has not reached the end

        first walk r pointer n steps ahead. This means the gap between r and n should be n + 1
            for this, set a counter to 1
            while this counter is not at n+1, keep walking r

        Now that r is at n+1 node in LL, walk both c and r untill r has reached the end.

        This way, r hits the end, c will be at n th node of list



    '''

    r=c=head
    i=1
    # r=c.next

    while r!= None:

        while i != n+1:
            r = r.next
            i += 1
            if r == None:
                return None

        c = c.next
        r = r.next

    return c.value

a = Node(7)
b = Node(14)
c= Node(21)
d = Node(28)

head=a
a.next=b
b.next=c
c.next=d


print_linked_list(head)
print("sdf")
print(return_last_nth_node(head,10))
