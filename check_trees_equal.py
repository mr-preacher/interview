# Python implementation to check if
# given 2 binary tries are equal
# recursive and iterative solutions

# A binary tree node containing data
# field, left and right pointers


class Node:
    # constructor to create new node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def is_tree_equal(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False

    return (node1.data == node2.data
            and is_tree_equal(node1.left, node2.left)
            and is_tree_equal(node1.right, node2.right))


def is_tree_equal_iterative(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False

    queue1 = [node1]
    queue2 = [node2]

    while len(queue1) > 0 and len(queue2) > 0:
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)

        if node1.data != node2.data:
            return False

        if node1.left is not None and node2.left is not None:
            queue1.append(node1.left)
            queue2.append(node2.left)
        elif node1.left is not None or node2.left is not None:
            return False

        if node1.right is not None and node2.right is not None:
            queue1.append(node1.right)
            queue2.append(node2.right)
        elif node1.right is not None or node2.right is not None:
            return False

    return True


# order by branch from left to right
root1 = Node(1)
root1.left = Node(2)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.left.right.left = Node(6)
root1.right = Node(3)
root1.right.right = Node(7)

# order by level from lefts to rights
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.right = Node(7)
root2.left.right.left = Node(6)

if is_tree_equal(root1, root2):
    print("Both trees are identical")
else:
    print("Trees are not identical")

print("Iterative:")
if is_tree_equal_iterative(root1, root2):
    print("Both trees are identical")
else:
    print("Trees are not identical")
