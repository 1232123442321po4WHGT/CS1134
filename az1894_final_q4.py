class LinkMinHeap:
    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

    class Item:
        def __init__(self, priority, value = None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority
        
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        item = self.root.item 
        return item

    def last_node(self):
        path = bin(self.size)[3:]
        curr = self.root
        for item in list(path):
            if item == '0':
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def last_path(self):
        ret =  bin(self.size)[3:]
        if ret == '':
            return None
        return ret

    def next_open(self):
        ret = bin(self.size + 1)[3:]
        if ret == '':
            return None
        return ret

    def parent(self, path):
        if path == None:
            return None
        elif path == 0 or path == 1:
            return None
        
        return self.shiftright(path)

    def shiftleft(self, path):
        if (path == None):
            path = '0'
        else:
            path += '0'
        return path

    def shiftright(self, path):
        pathlist = list(path)
        newpath = pathlist[:-1]
        return newpath

    def leftchild(self, path):
        return self.shiftleft(path)

    def rightchild(self, path):
        path = self.shiftleft(path)
        return path

    def path_list(self, path):
        return list(path)

    def nodefinder(self, path):
        curr_node = self.root
        if path == None:
            return curr_node
        for item in self.path_list(path):
            if item == '0':
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node

    def printree(self):
        def traverse(root):
            if (root is None):
                pass
            else:
                traverse(root.left)
                traverse(root.right)
                print(root.item.priority, root.item.value)
        traverse(self.root)

    def insert(self, priority, value = None):
        open_path = self.next_open()
        new_item = LinkMinHeap.Item(priority, value)
        new_node = LinkMinHeap.Node(new_item)
        new_node.left = None
        new_node.right = None
        parentpath = self.parent(open_path)
        new_node.parents = self.nodefinder(parentpath)
        
        if parentpath == None:
            self.root = new_node
        else:
            if new_node.parents.left == None:
                new_node.parents.left = new_node
            else:
                new_node.parents.right = new_node
        
        self.size += 1

        self.fix_up(open_path)

    def fix_up(self, path):
        curr_path = path
        keep_going = True
        while (keep_going == True and curr_path != None):
            parent_path = self.parent(curr_path)
            curr_node = self.nodefinder(curr_path)
            parent_node = self.nodefinder(parent_path)
            if (curr_node.item < parent_node.item):
                self.swap(curr_path, parent_path)
                curr_path = parent_path
            else:
                keep_going = False
    
    def delete_min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        path1 = None
        path2 = self.last_path()
        self.swap(path1, path2)

        lastnode = self.nodefinder(path2)
        returnval = lastnode.item

        if path1 == path2:
            self.root = None
        else:
            if lastnode.parents.right == None:
                lastnode.parents.left = None
            else:
                lastnode.parents.right = None

            self.fix_down(None)
        
        del lastnode

        self.size -=1
        return returnval

    def fix_down(self, path):
        curr_path = path
        keep_going = True
        while(keep_going == True):
            curr_node = self.nodefinder(curr_path)
            if curr_node.left == None and curr_node.right == None:
                keep_going = False
            elif curr_node.right == None:
                if curr_node.left.item < curr_node.item:
                    self.swap(curr_path, self.leftchild(curr_path))
                    curr_path = self.leftchild(curr_path)
                keep_going = False
            else:
                if curr_node.left.item < curr_node.right.item:
                    small_child_path = self.leftchild(curr_path)
                else:
                    small_child_path = self.rightchild(curr_path)

                if self.nodefinder(small_child_path).item < curr_node.item:
                    self.swap(curr_path, small_child_path)
                    curr_path = small_child_path
                else:
                    keep_going = False
                

    def swap(self, path1, path2):
        node1 = self.nodefinder(path1)
        node2 = self.nodefinder(path2)
        node1.item, node2.item = node2.item, node1.item

def main():
    h = LinkMinHeap()

    h.insert(3,3)
    h.insert(1,1)
    h.insert(3,3)

    print(len(h))
    
    h.printree()
    print('--')
    print(h.min().priority)
    print(h.delete_min().priority) 

    print(h.min().priority)
    print(h.delete_min().priority)

    print(h.min().priority)
    print(h.delete_min().priority)
