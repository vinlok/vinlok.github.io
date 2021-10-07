
'''

create a queue
set queue first ele to be arrays first element
set c=0
l=-4
iterate over each element of array:
    - counter += 1
    - if a[i] > l
        l = a[i]
    - if counter = window_size:
        print(l)
        counter=w-1


    - pop(right) from the queue
    - if a[i] > popped:
        append a[i] to stack

2,10,-5,3,6


-4 2 -5 = 10, 2

 2 -5 3 = 3

 -5 3 u



 algo:

 brute force

set s to size of window
set pointer1 to 0
set pointer2 to p1 + s

while true:
    m=a[p1]
    iterate over elemets from p1 to p2:




'''

a= [-4,2,-5,3,6]
s=3
p1 = 0
p2 = p1 + s

while True:
    m=a[p1]
    for i in range(p1,p2):
        m=max(a[i],m)

    print(m)

    p1 += 1
    p2 += 1

    if(p2 > len(a)):
        break;



