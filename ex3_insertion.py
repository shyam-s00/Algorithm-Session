from pprint import pprint

def insertionSort(nums: list):
    for i in range(1, len(nums)):               # we are going to take the first element (one element in a list is considered to be sorted.) and compare it with
        for j in range(i):                      # other elements to the right side of it. Left side is considered to be sorted and right side is considered as 
            if nums[i] < nums[j]:               # unsorted list. 
                item = nums.pop(i)              # For each iteration, we take the first element from the unsorted section and compare them from the beginning 
                nums.insert(j, item)            # of the sorted list section. When we find a right place for the number, we will insert it in respective location. 
                #pprint(nums)
    return nums