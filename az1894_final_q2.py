from LinkedBinaryTree import LinkedBinaryTree

def count_mono_data_subtrees(bin_tree):
    count = 0
    def count_mono_data_subtrees_helper(root):
      # returns true if the subtree at root is a mono subtree
        nonlocal count
        # at an empty root
        if root is None:
            return True

        left = count_mono_data_subtrees_helper(root.left) # True if left is a mono subtree
        right = count_mono_data_subtrees_helper(root.right)  # True if right is a mono subtree

        if left == False or right == False:
            return False

        if root.left and root.left.data != root.data:
            return False

        if root.right and root.right.data != root.data:
            return False

        count += 1
        return True

    count_mono_data_subtrees_helper(bin_tree.root)

    return count

leaf7 = LinkedBinaryTree.Node(7)

leaf8 = LinkedBinaryTree.Node(8)
test7 = LinkedBinaryTree.Node(7)




root7 = LinkedBinaryTree.Node(7, leaf7, test7)
root4 = LinkedBinaryTree.Node(4, None, None)
root5 = LinkedBinaryTree.Node(5, None, leaf8)

root3 = LinkedBinaryTree.Node(3, root7, None)
root3_2 = LinkedBinaryTree.Node(3, root4, root5)

baseroot = LinkedBinaryTree.Node(1, None, None)

base = LinkedBinaryTree(root = baseroot)

print(count_mono_data_subtrees(base))