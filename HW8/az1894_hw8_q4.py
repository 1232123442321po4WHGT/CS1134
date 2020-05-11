from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    min_diff = 99999999999999
    
    root = bst.root
    def recur_tree(node, great_ancestor, min_diff):
        if node == None:
            return min_diff

        if node.parent != None and great_ancestor != None:
            parent_minus = node.item - node.parent.item
            if parent_minus <0:
                parent_diff = parent_minus * -1
            else:
                parent_diff = parent_minus
            great_ancestor_minus = node.item - great_ancestor.item
            if great_ancestor_minus < 0:
                great_ancestor_diff = great_ancestor_minus * -1
            else:
                great_ancestor_diff = great_ancestor_minus
            if parent_diff < min_diff:
                min_diff = parent_diff
            if great_ancestor_diff < min_diff:
                min_diff = great_ancestor_diff

        if node.parent == None:
            return min(recur_tree(node.left , node , min_diff) , recur_tree(node.right , node , min_diff))
        return min(recur_tree(node.left , node.parent , min_diff) , recur_tree(node.right , node.parent , min_diff))
    return recur_tree(root , None , min_diff)