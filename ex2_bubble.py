def bubblesort(lst):
    while True:                                 # we are going to loop through the list till we get an iteration without any swap
        swap = False
        for y in range(0, len(lst) - 1):        # In this inner loop, we are going to compare two elements next to each other (from the beginning)
            if lst[y] > lst[y+1]:               # A swap will be made if the numbers are in out of place. (Unsorted order... )
                temp = lst[y+1]                 # if a swap is done, we will continue the outer loop one more time till there is
                lst[y+1] = lst[y]               # no swap.
                lst[y] = temp
                swap = True
        
        if swap == False:                       # when we get here, we have come to an iteration without any swap and list is sorted.
            break
    return lst