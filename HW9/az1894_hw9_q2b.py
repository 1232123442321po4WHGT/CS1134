import ChainingHashTableMap

def intersection_listb(lst1, lst2):
    hash_map = ChainingHashTableMap.ChainingHashTableMap()
    return_list = []
    for key in lst1:
        hash_map[key] = True

    for key in lst2:
        try:
            if hash_map[key] != False:
                return_list.append(key)
        except:
            raise Exception('')

    return return_list