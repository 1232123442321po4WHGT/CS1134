from BinarySearchTreeMap import BinarySearchTreeMap
def restoreHelper(low, high, lst):
        temp = -1
        if low >= high:
            bst1 = BinarySearchTreeMap()
            returnval = bst1.Node(bst1.Item(lst[low]))
            return returnval
        else:
            low += 1
            high += 1

            bottom = low
            done = False
            while done == False:
                if lst[low] < lst[bottom]:
                    tempval = bottom
                    done = True
                bottom += 1
            
            lowval = bst1.Item(lst[low])
            noderoot = bst1.Node(lowval)
            if tempval == -1:
                tempval = high + 1
            else:
                noderoot.left = restoreHelper(low + 1, temp - 1, lst)
                noderoot.right = restoreHelper(temp, high, lst)
            return noderoot

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst) > 0:
        bst.root = restoreHelper(0, len(prefix_lst) - 1, prefix_lst)
    return bst