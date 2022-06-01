my_list = ['20.05.01', '19.03.21', '18.07.31', '22.01.01','21.04.03']
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


print(quicksort(my_list))