import unittest

# finds and returns the k-th smallest element in the given array
def linear_selection(values, k):
    size = len(values)
    if k < 0 or k > size:
        return None
    if size == 1:
        return values[0]
    # slice
    parts = slice_in_groups_of_five(values)
    # find the median of each group
    print(size)
    medians_array = find_medians_array(parts, size)
    print("medians: " + str(medians_array))
    # find the median of medians
    total_medians = len(medians_array)
    median = linear_selection(medians_array, (total_medians//2))

    # partition original data around the median of medians
    lesser, greater = partition_set(values, median)

    lesser_size = len(lesser)
    print("median: " + str(median))
    print("greater: " + str(greater))
    print("lesser: " + str(lesser))
    # base case for the recursion
    if lesser_size == k-1:
        return median
    # recursive calls to find the element    
    if lesser_size > k-1:
        return linear_selection(lesser, k)
    if lesser_size < k-1:
        return linear_selection(greater, k-lesser_size-1)

# slice the given array into groups of five
def slice_in_groups_of_five(values):
    totalSize = len(values)
    num_of_groups = totalSize // 5

    if num_of_groups == 0:
        return [values]

    arrays = []
    iteration = 1
    for i in range(0,totalSize, 5):
        leftMargin = i
        rightMargin = (iteration * 5)
        arrays.append(values[leftMargin:rightMargin])
        iteration += 1
    
    return arrays

# sort each array in an array
def sort_array_of_arrays(values):
    sorted_values = []
    for value in values:
        value.sort()
        sorted_values.append(value)

    return sorted_values

# find the medians in an array
def find_median(values):
    half = len(values) // 2
    return values[half]

# find the medians in each array
def find_medians_array(values, size):
    sorted_arrays = sort_array_of_arrays(values)
    medians_array = []
    floor = size // 5
    if floor == 0:
        median = find_median(values[0])
        return [median]
        
    for i in range(0, floor):
        median = find_median(values[i])
        medians_array.append(median)
        
    return medians_array

# partition data set, returning a set where all numbers are less then median and a set where all the numbers are greater than median
def partition_set(values, median):
    lesser = []
    greater = []

    for value in values:
        if value < median:
            lesser.append(value)
        elif value > median:
            greater.append(value)
    
    return lesser, greater

# Tests
class Tests(unittest.TestCase):
    def test_slice_in_groups_of_five(self):
        passed_array = [1,2,3,4,5,6,7,8,81,65,41,99,312,32,61,23,654,23,11,58,33,123,34,12]
        result = slice_in_groups_of_five(passed_array)
        expected_arrays = [[1, 2, 3, 4, 5], [6, 7, 8, 81, 65], [41, 99, 312, 32, 61], [23, 654, 23, 11, 58], [33, 123, 34, 12]]

        self.assertEqual(result, expected_arrays, "Didn't split array successfully")
    
    def test_sort_array_of_arrays(self):
        passed_array = [[1,2,3,4,5], [6,7,8,81,65]]
        result = sort_array_of_arrays(passed_array)
        expected_arrays = [[1, 2, 3, 4, 5], [6, 7, 8, 65, 81]]

        self.assertEqual(result, expected_arrays, "Didn't order arrays correctly")

    def test_find_median(self):
        passed_array = [1,2,3,4,5]
        result = find_median(passed_array)
        expected_result = 3

        self.assertEqual(result, expected_result, "Didn't find the median correctly")

    def test_find_medians_array_full(self):
        passed_array = [[1,2,3,4,5], [6,7,8,65,81]]
        result = find_medians_array(passed_array, 10)
        expected_result = [3,8]

        self.assertEqual(result, expected_result, "Didn't generate the medians array correctly for full arrays")

    def test_find_medians_array_extras(self):
        passed_array = [[1,2,3,4,5], [6,7,8]]
        result = find_medians_array(passed_array, 8)
        expected_result = [3]

        self.assertEqual(result, expected_result, "Didn't generate the medians array correctly for arrays with extras")

    def test_partition_set(self):
        passed_array = [1,49,92,43,67,5,8,6,81] # [1,5,6,8,43,49,67,81,92] -> median is 43
        lesser, greater = partition_set(passed_array, 43)
        expected_lesser = [1,5,8,6]
        expected_greater = [49,92,67,81]

        self.assertEqual(lesser, expected_lesser, "Didn't match lesser set correctly")
        self.assertEqual(greater, expected_greater, "Didn't match greater set correctly")

    def test_ultimate_integration(self):
        passed_array = [1,2,3,4,5,6,7,8,81,65,41,99,312,32,61,23,654,23,11,58,33,123,34,12]
        element = linear_selection(passed_array, 13)
        expectedElement = 32

        self.assertEqual(element, expectedElement, "Didn't match expected element in ultimate integration test")


unittest.main()