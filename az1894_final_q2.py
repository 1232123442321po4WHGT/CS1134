from LinkedBinaryTree import LinkedBinaryTree

def count_mono_data_subtrees(bin_tree):
    count = 0
    def count_mono_data_subtrees_helper(root):
      # returns true if the subtree at root is a mono subtree
        nonlocal count
        # at an empty root
        if root is None:
            return True

        leftmono = count_mono_data_subtrees_helper(root.left) # True if left is a mono subtree
        rightmono = count_mono_data_subtrees_helper(root.right)  # True if right is a mono subtree

        if leftmono == False or rightmono == False:
            return False

        if root.left != None and root.left.data != root.data:
            return False

        if root.right != None and root.right.data != root.data:
            return False

        count += 1
        return True

    count_mono_data_subtrees_helper(bin_tree.root)

    return count

l54 = LinkedBinaryTree.Node(4)
l5_24 = LinkedBinaryTree.Node(4)

l47 = LinkedBinaryTree.Node(7)
l44 = LinkedBinaryTree.Node(4)
l4_24 = LinkedBinaryTree.Node(4, l54, l5_24)
l48 = LinkedBinaryTree.Node(8)

l37 = LinkedBinaryTree.Node(7, l47, None)
l34 = LinkedBinaryTree.Node(4, l44, l4_24)
l35 = LinkedBinaryTree.Node(5, None, l48)

l23 = LinkedBinaryTree.Node(3, l37, None)
l2_23 = LinkedBinaryTree.Node(3, l34, l35)

baseroot = LinkedBinaryTree.Node(1, l23, l2_23)

base = LinkedBinaryTree(root = baseroot)

print(count_mono_data_subtrees(base))

