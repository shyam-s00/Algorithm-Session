import unittest
from ex2_bubble import bubblesort
from ex3_insertion import insertionSort
from ex4_merge import mergeSort
from ex5_quick import quickSort

class SortingTests(unittest.TestCase):
    def setUp(self):
        self.list1 = [10, 5, 7, 2, 3, 9, 8, 4, 6, 1]
        self.list2 = [5, -1, 4, -2, -4, 0, 2, 1, 3, -3]
        self.sortedList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.sortedList2 = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    def test_bubblesort(self):
        self.assertListEqual(bubblesort(self.list1), self.sortedList1)
        self.assertListEqual(bubblesort(self.list2), self.sortedList2)
        
    def test_insertionsort(self):
        self.assertListEqual(insertionSort(self.list1), self.sortedList1)
        self.assertListEqual(insertionSort(self.list2), self.sortedList2)

    def test_mergesort(self):
        self.assertListEqual(mergeSort(self.list1), self.sortedList1)
        self.assertListEqual(mergeSort(self.list2), self.sortedList2)

    def test_quicksort(self):
        self.assertListEqual(quickSort(self.list1), self.sortedList1)
        self.assertListEqual(quickSort(self.list2), self.sortedList2)