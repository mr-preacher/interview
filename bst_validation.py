# Python implementation to check if 
# given Binary tree is a BST or not

# A binary tree node containing data
# field, left and right pointers

class Node:
    # constructor to create new node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    

# function to check if given binary
# tree is BST
def isbst(root, min, max):
    
    if root is None:
        return True

    # left tree
    if root.data < min or root.data > max:
       return False 

    return isbst(root.left, min, root.data - 1) and isbst(root.right, root.data + 1, max)


# driver code to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isbst(root,-pow(2, 32)-1,pow(2, 32)):
    print("is BST")
else:
    print("not a BST")