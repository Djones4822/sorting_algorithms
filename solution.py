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
    
    
def bubble_sort(unsorted_list):
    a_list = list(unsorted_list)
    list_length = len(a_list)
    
    # iterate over the list
    for i in range(list_length):
        # iterate over the unsorted part of the list
        for j in range (i+1, list_length):
            if a_list[j] < a_list[i]:
                # swap
                a_list[i], a_list[j] = a_list[j], a_list[i]
    return a_list
