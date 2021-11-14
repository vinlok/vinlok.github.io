class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None




def print_linked_list(head):
    cur_node=head
    while cur_node != None:
        print(cur_node.value,end="->")
        cur_node=cur_node.next



def merge_lists(head1,head2):

    '''
     Algo:
     1. Start with c1=head1 and c2=head2
     2. create a merged list head with None value. c3=new_none_node
     3. while both the list have not been exhausted
        compare the value of c1 and c2.
        whichever is small, add that to the c3.next
        and move the smaller one by one step
    '''

    c1=head1
    c2=head2
    m_l=None
    c3=m_l


    exhausted_c1=exhausted_c2=False
    # Walk upto nth node
    while c1 != None or c2 != None:

        if c1 == None:
            c3.next = c2
            break;

        if c2 == None:
            c3.next = c1
            break;
        # print(c1.value,c2.value,"--")
        if c1.value < c2.value:
            print("here")
            if m_l == None:
                print(f"+{c1.value}")
                m_l=Node(c1.value)
                c3=m_l
            else:
                print(f"++{c1.value}")
                c3.next=Node(c1.value)
                c3=c3.next
            print_linked_list(m_l)
            c1=c1.next
        else:
            print("here1")
            if m_l == None:
                print(f"-{c2.value}")
                m_l=Node(c2.value)
                c3=m_l
            else:
                print(f"--{c2.value}")
                print(c3.value)
                c3.next=Node(c2.value)
                c3=c3.next
                print(c3.value,"sdfsdf")
            c2=c2.next

    print("----")
    print_linked_list(m_l)
    print("-----")
    return(m_l)

a = Node(15)
b = Node(19)
c= Node(22)


head1=a
a.next=b
b.next=c



a = Node(9)
b = Node(10)
c= Node(16)


head2=a
a.next=b
b.next=c


# print_linked_list(head1)
# print_linked_list(head2)

print("-------")

print_linked_list(merge_lists(head1,head2))