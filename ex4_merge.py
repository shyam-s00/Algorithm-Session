def mergeSort(nums):                                            # Uses Divide and Conquer Strategy.

    if len(nums) < 2:                                           # Split the list until it can't be splited any further. (Contains only one element)
        return nums

    median = len(nums) // 2                                     # with the median value, list is split into two half --> left and right from the median value. 
    left = nums[:median]
    right = nums[median:]

    return stitch(mergeSort(left), mergeSort(right))


def stitch(left: list, right: list):                            # stitch or merge algorithm, joins two sorted lists into one (new list is created). 
    results = []

    while len(left) and len(right):                             # Take first element from one list and compare it with first element in another. 
        if left[0] <= right[0]:                                 # Add the smaller value to newly constructed list and remove it from the source. (left / right)
            results.append(left.pop(0))                     
        else:
            results.append(right.pop(0))                        # repeat this until one of the list (left or right) becomes empty. 

    results = results + left + right                            # finally just append the remaining list to the newly constructed list. At this point either left 
    return results                                              # or right is empty and one which has the remaining values is sorted and can be added to the result list