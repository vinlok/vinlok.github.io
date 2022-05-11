# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

from collections import deque
import pdb

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        currentNode = self

        while True:
            #here 12 will be passes to the value argument
            #currentNode first time will be root
            print(f"current node is: {currentNode.value}")
            if value < currentNode.value:
                if currentNode.left == None:
                    print(f"inserting node to left of {currentNode.value}")
                    currentNode.left = BST(value)
                    break;
                else:
                    currentNode = currentNode.left
            else    :
                if currentNode.right == None:
                    print(f"inserting node to right of {currentNode.value}")
                    currentNode.right = BST(value)
                    break;
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        # Write your code here.

        currentNode = self
        while True:
            if currentNode.value == value:
                return True
            elif value > currentNode.value:
                if currentNode.right == None:
                    break
                currentNode = currentNode.right
            else:
                if currentNode.left == None:
                    break
                currentNode = currentNode.left
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.


        return self

    def getMinValue(self):

        currentNode = self
        while True:

            if currentNode.left == None:
                return currentNode.value

            else:
                currentNode = currentNode.left



def branchSums(root):
    sums=[]
    calculateBranchSums(root,0,sums)
    return sums


def calculateBranchSums(node,rs,sums):

    if node is None:
        return

    ns=rs + node.value
    if node.left is None and node.right is None:
        sums.append(ns)
        return

    # print(node.left.value)
    calculateBranchSums(node.left,ns,sums)
    # print(node.right.value)
    calculateBranchSums(node.right,ns,sums)

def print_tree(root):

    c_l=deque()
    n_l=deque()

    c_l.append(root)

    level = 0
    while len(c_l) != 0:
        print(f"current Level: {level}. Number of element:{len(c_l)}")
        for i in range(len(c_l)):
            node = c_l.popleft()
            print(node.value,end=" ")

            if node.left:
                n_l.append(node.left)

            if node.right:
                n_l.append(node.right)

        print("")
        level+=1
        c_l=n_l
        n_l=deque()


def cal_tree_sum(root):
    '''

    DFS traversal with stack

    1. Create a empty stack. Stack will be storing {current_node:sum_upto_that_node}
    2. set the current_node to root and sum_upto=0
       create sums=[]
    3. while all nodes are not traveresed or done
        4. if current_node is not null
            5. sumupto=sumupto+current_node.value
            6. append {current_node:sumupto} to the stack
            7. move left by settting current_node = current_node.left
        8. else:
            if the stack is not empty
               then pop from stack and set current_node to popped val
               append sumupto from the popped to sums
               move right current_node.right
            else
                return

    '''


    stack=deque()
    current_node= root
    sum_upto=0
    sums=[]
    done = False
    while done != True:
        # print(current_node.value)
        if current_node != None:
            sum_upto=sum_upto+current_node.value
            stack.append((current_node,sum_upto))
            current_node=current_node.left

        else:
            if len(stack) != 0:
                print(stack)
                (current_node,sum_upto)=stack.pop()
                print(current_node,sum_upto)

                if current_node.left == None and current_node.right == None:
                    sums.append(sum_upto)

                current_node=current_node.right
            else:
                done=True

    print(sums)






root = BST(10)



root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(6)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
# print_tree(root)
# print(branchSums(root))
cal_tree_sum(root)