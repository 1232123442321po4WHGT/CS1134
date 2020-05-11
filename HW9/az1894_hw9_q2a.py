

#Part A
def intersection_lista(lst1, lst2):
    return_list = []
    for num1 in lst1:
        for num2 in lst2:
            if num1 == num2:
                return_list.append(num1)

    return return_list