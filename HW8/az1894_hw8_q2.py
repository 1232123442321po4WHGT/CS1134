from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for num in range(1, n + 1):
        bst.insert(num, num)
    return bst

def add_items(bst, low, high): 
    if low == high:
        item = BinarySearchTreeMap.Item(low)
        node = BinarySearchTreeMap.Node(item)

    else:
        mid = (low + high) // 2

        item = BinarySearchTreeMap.Item(mid)
        node = BinarySearchTreeMap.Node(item)
        
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)

    return node

# Runtime function for part 1 is n^2, since there are n iterations for n elements. What you get is an equation of [1+ 2+ 3+.....+(n-1)] / 2, which is O(n^2).
# Runtime function for part 2 is n log n, you're having an average depth traversed on average, for N elements. This means that you have nodes n=2^k - 1
# giving a k = log2(n+1), then multiplying by n elements gives nk = nlog2(n+1), which is O(nlogn)