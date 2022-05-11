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



def bfs_print_tree(root):
    '''
        1. Create two stacks: current_level and next_level
        2. Add root node to the current_level
        3. While the len(current_level) is not zero
            4. For all the nodes in the current_level:
                5. popleft the node from current_level and do the business logic here.
                6. If it has left and right nodes add them to next_level
                7. make current_level as next_level
                8. make next_level empty
    '''

    current_level = deque()
    next_level = deque()

    current_level.append(root)

    while len(current_level) != 0:
        for i in range(len(current_level)):
            node=current_level.popleft()
            print(node.value,end=" ")
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        current_level=next_level
        next_level=deque()
        print("")


def are_bst_identical(root1,root2):
    '''
    Do DFS on both trees comparing the nodes everytime. Use stacks to do dfs

    1. create stacks for both trees stack1 stack2
    2. set the tree1_current_node=root1 and tree2_current_node=root2
    3. While we are not done traversing all nodes of tree1 do the following. Logic is that if trees are identical we traversing one and comparing other should work.
        4. if the tree1_current_node is not None:
            then
                compare the value of tree1_current_node and tree2_current_node
                    if same
                        then
                            add tree1_current_node to stack1
                            add tree2_current_node to stack2
                            tree1_current_node walk left
                        else
                            say tree are not identitical
            else
                if len(stack1) != 0
                    then
                        tree1_current_node=stack1.pop()
                        tree2_current_node=stack2.pop()
                        compare the current nodes again.
                        if same walk both to right
                        else say tree not identitical
                else
                    we are done traversing all nodes
                    return true saying tree are identitical

    '''


    stack1 = deque()
    stack2 = deque()

    t1_cur_node = root1
    t2_cur_node = root2

    done = False

    while done != True:

        if t1_cur_node != None:
            if t1_cur_node.value == t2_cur_node.value:
                stack1.append(t1_cur_node)
                stack2.append(t2_cur_node)
                t1_cur_node = t1_cur_node.left
                t2_cur_node = t2_cur_node.left
            else:
                print(f"{t1_cur_node.value} not matching with {t2_cur_node.value}")
                return False

        else:
            if len(stack1) != 0:
                t1_cur_node = stack1.pop()
                t2_cur_node = stack2.pop()
                if t1_cur_node.value == t2_cur_node.value:
                    t1_cur_node=t1_cur_node.right
                    t2_cur_node=t2_cur_node.right
                else:
                    print(f"{t1_cur_node.value} not matching with {t2_cur_node.value}")
                    return False
            else:
                done=True
                print("Identitical")
                return True

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(6)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

bfs_print_tree(root)

root1 = BST(11)
root1.left = BST(5)
root1.left.left = BST(2)
root1.left.left.left = BST(1)
root1.left.right = BST(6)
root1.right = BST(15)
root1.right.left = BST(13)
root1.right.left.right = BST(14)
root1.right.right = BST(22)

bfs_print_tree(root1)

are_bst_identical(root,root1)
# print_tree(root)

# print(branchSums(root))
#dfs_no_recurse(root)