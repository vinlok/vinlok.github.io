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
            # here 12 will be passes to the value argument
            # currentNode first time will be root
            print(f"current node is: {currentNode.value}")
            if value < currentNode.value:
                if currentNode.left == None:
                    print(f"inserting node to left of {currentNode.value}")
                    currentNode.left = BST(value)
                    break;
                else:
                    currentNode = currentNode.left
            else:
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
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, rs, sums):
    if node is None:
        return

    ns = rs + node.value
    if node.left is None and node.right is None:
        sums.append(ns)
        return

    # print(node.left.value)
    calculateBranchSums(node.left, ns, sums)
    # print(node.right.value)
    calculateBranchSums(node.right, ns, sums)


def print_tree(root):
    c_l = deque()
    n_l = deque()

    c_l.append(root)

    level = 0
    while len(c_l) != 0:
        print(f"current Level: {level}. Number of element:{len(c_l)}")
        for i in range(len(c_l)):
            node = c_l.popleft()
            print(node.value, end=" ")

            if node.left:
                n_l.append(node.left)

            if node.right:
                n_l.append(node.right)

        print("")
        level += 1
        c_l = n_l
        n_l = deque()


def dfs_no_recurse(root):

    '''
        #1 Create an empty stack to track the nodes of the tree

        #2 Set current node to the root of the tree

        #3 while all nodes are not traverse or not done

            if the current node is not None
            #4 Add the current node to the stack
            #5 Walk to left by moving current node to left

            else
                if the stack is not empty
                    then
                        set current node as pop from stack
                        do custom logic
                        move to right by setting current node to currentnode.right

                else if stack empty
                    then you are done

    '''

    stack = deque()

    current_node = root

    done = False

    while not done:

        if current_node != None:
            stack.append(current_node)
            current_node=current_node.left

        else:
            if len(stack) != 0:
                current_node = stack.pop()

                print(current_node.value)

                current_node = current_node.right
            else:
                done = True


def print_leaf(root):
    '''
    do dfs, when you pop, see if it is leaf or not
    :param root:
    :return:
    '''

    stack=deque()
    cur_node=root
    done=False

    while done != True:
        if cur_node != None:
            stack.append(cur_node)
            cur_node=cur_node.left

        else:
            if len(stack) != 0:
                cur_node=stack.pop()

                if cur_node.left == None and cur_node.right == None:
                    print(cur_node.value)
                cur_node=cur_node.right
            else:
                done=True



def print_perimeter(root):

    '''

    algo1:
    Do BFS, print root then for each level, while going from left to right, print first, then for the middle sea if they are leaf, if leaf, print them, else print last.

    Algo2:
    do DFS, print root, then go down to left side printing elements until you hit leaf, then backtrack to node with right branch and print leaf,if root found after popping or during backtracking, then you are going to the rightside of the tree



    1. Initialize empty stack
    2. set current_node to root.
    3. While not done
        - if the current_node is not None:
            - append current_node to stack
            - move left

        - else
            - if the stack not empty:
                - cur_node is pop of stack (last element of stack)
                - for iord traversal do business logic here
                - move right of current node


    :param root:
    :return:
    '''

def print_left(root):
    cur_node=root

    done = False
    while done is not True:

        if cur_node.left != None:
            cur_node = cur_node.left
        elif cur_node.right != None:

            cur_node = cur_node.right
        else:
            # done = True
            break

        if cur_node.left == None and cur_node.right == None:
            print("found leaf")
        else:
            print(cur_node.value)


    # while cur_node.left != None:
    #
    #     cur_node = cur_node.left
    #     if cur_node.left != None and cur_node.right != None:
    #         print(cur_node.value)
    #     else:
    #
    #         print(f"{cur_node.value} found left leaf")



def print_right_no_leaf(root):
    cur_node=root

    while cur_node.right!=None:

        cur_node = cur_node.right
        if cur_node.left != None and cur_node.right != None:
            print(cur_node.value)
        else:
            print("found right leaf")


def print_right(root):
    print(root.value)
    cur_node=root
    while True:

        if cur_node.right != None:
            cur_node=cur_node.right
            print(cur_node.value)

        elif cur_node.left != None:
            cur_node=cur_node.left
            print(cur_node.value)
        else:
            break


def print_left(root):
    print(root.value)
    cur_node=root
    while True:

        if cur_node.left != None:
            cur_node=cur_node.left
            print(cur_node.value)

        elif cur_node.right != None:
            cur_node=cur_node.right
            print(cur_node.value)
        else:
            break

root = BST(10)
root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
root.left.right = BST(7)
root.left.right.left = BST(6)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
# print_tree(root)

# print(branchSums(root))
# dfs_no_recurse(root)

#
# print(root.value)
# print("left")
# print_left(root)
# print("leaves")
# print_leaf(root)
# print("right")
# print_right_no_leaf(root)


print_right(root)
print_left(root)