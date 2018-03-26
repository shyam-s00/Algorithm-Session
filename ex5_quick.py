def quickSort(nums):                                            # Uses divide and conquer strategy (just like merge sort...)
    if len(nums) < 2:                                           # If the length of the list is less than two, it can't be splitted any further and it is considered 
        return nums                                             # to be sorted already.

    pivot = nums[-1:]                                           # Take a pivot element from the list (best approach is to take the last element on the list.). However, 
    left, right = [], []                                        # there are other variations of this sort in which a different pivot is choosen based on the requirement. 

    for x in range(len(nums) - 1):                              # Sorting happens by comparing each element in the list to the pivot element choosen. 
        if nums[x] < pivot[0]:                                  # if the number is less than the pivot element, put it in the left array
            left.append(nums[x])
        else:
            right.append(nums[x])                               # if the number is greater than the pivot element, put it in the right array.

    return quickSort(left) + pivot + quickSort(right)           # Merge the left + pivot + right array to get the sorted array.