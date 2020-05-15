from ArrayStack import ArrayStack
from ChainingHashTableMap import ChainingHashTableMap
    
def construct_a_longest_palindrome(numbers_bank):
    s = ArrayStack()
    t = ChainingHashTableMap()
    for elem in numbers_bank:
        try:
            t.__getitem__(elem)
            del t[elem]
            s.push(elem)

        except:
            t[elem] = elem
    #print_hash_table(t)

    if t.is_empty() == False:
        single = True
        iterations = t.__iter__()
        item = iterations.__next__()
        del t[item]
        s.push(item)
    else:
        single = False
    
    if single == True:
        final = []
        middle = s.pop()
        final.append(middle)
        while s.is_empty() == False:
            ends = s.pop()
            edge = [ends]
            final = edge + final + edge

    else:
        final = []
        while s.is_empty() == False:
            ends = s.pop()
            edge = [ends]
            final = edge + final + edge
    
    return final

print(construct_a_longest_palindrome([3, 47, 6, 6, 5, 6, 15, 3, 22, 1, 6, 15]))
print(construct_a_longest_palindrome([]))
print(construct_a_longest_palindrome([1,1,3,2,3,2]))

#Runtime analysis: I'll be going over n terms in the list, meaning that I'll be running n time off the bat. For each number, I'll be searching the hash table
# which is constant time. Adding and deleting from the hash table is constant time. For the stacks, I'm adding n time to it, for when we're adding and poping
# from the stacks. Once popped from the stack, list concantenation is n time, giving a total runtime for the whole list to be n time. 