#insertion sort

def insertion_sort(a_lst):
    lst = a_lst
    #go through each list element except the first (which is trivially sorted)
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i
        #now go through the rest of the list, we know that lst[:i] is sorted by default
        while j > 0 and lst[j-1] > temp:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = temp
    return lst
