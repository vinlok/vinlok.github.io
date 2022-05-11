class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


def create_list(l):
    h=Node(l[0])
    c=h
    for i in range(1,len(l)):
        n_n=Node(l[i])
        c.next=n_n
        c=n_n
    return h

def print_list(h):
    c=h
    while c!=None:
        print(c.value)
        c=c.next

def insert_into_sl(h,pos,v):

    c=h
    count=0
    p=None
    while c != None:
        if count == pos:
            n_n=Node(v)
            p.next=n_n
            n_n.next=c
            return h
        p=c
        c=c.next
        count += 1


l=[1,2,3,4]
h=create_list(l)
print_list(h)
h1=insert_into_sl(h,1,5)

print_list(h1)
