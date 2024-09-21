"""
Problem Set 1.2
"""


## ADVANCED PROBLEM SET VERSION 1

# Problem 1: Transpose Matrix
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
    
    Parameters:
        matrix (list[list[int]]): 2D integer array
    
    Returns:
        list[list[int]]: transpose of matrix
    """
    pass

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(matrix)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose(matrix)


# Problem 2: Two-Pointer Reverse List
def reverse_list(lst: list) -> list:
    """
    Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
    Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

    Parameters:
        lst (list): list

    Returns:
        list: elements of lst in reverse order
    """
    pass

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# reverse_list(lst)

# Problem 3: Remove Duplicates
def remove_dupes(items: list) -> int:
    """
    Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

    Parameters:
        items (list): sorted array

    Returns:
        length of modified array after duplicates have been removed in-place
    """
    pass

# items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# remove_dupes(items)

# items = ["extract of malt", "haycorns", "honey", "thistle"]
# remove_dupes(items)


# Problem 4: Sort Array by Parity
def sort_by_parity(nums: list[int]) -> list:
    """
    Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.
    Return any array that satisfies this condition.
    
    Parameters:
        nums (list[int]): integer array

    Returns:
        list: any array that satisfies condition
    """
    pass

# nums = [3, 1, 2, 4]
# sort_by_parity(nums)

# nums = [0]
# sort_by_parity(nums)


# Problem 5: Container with Most Honey
def most_honey(height: list[int]) -> int:
    """
    Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most honey.
    Return the maximum amount of honey a container can store.
    
    Parameters:
        height (list[int]): integer array of length n

    Returns:
        int: maximum amount of honey a container can store
    """
    pass

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# most_honey(height)

# height = [1, 1]
# most_honey(height)


# Problem 6: Merge Intervals
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Parameters:
        intervals (list[list[int]]): array where intervals[i] = [starti, endi]

    Returns:
        list[list[int]]: array of non-overlapping intervals that cover all intervals in input
    """
    pass

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# merge_intervals(intervals)

# intervals = [[1, 4], [4, 5]]
# merge_intervals(intervals)


## ADVANCED PROBLEM SET VERSION 2

# Problem 1: Matrix Addition
def add_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Write a function add_matrices() that accepts two n x m matrices matrix1 and matrix2. The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

    Parameters:
        matrix1 (list[list[int]]): n x m matrix
        matrix2 (list[list[int]]): n x m matrix

    Returns:
        list[list[int]]: n x m matrix that is sum of given matrices at each value
    """
    pass

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# add_matrices(matrix1, matrix2)


# Problem 2: Two-Pointer Palindrome
def is_palindrome(s: str) -> bool:
    """
    Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.
    The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
    
    Parameters:
        s (str): string

    Returns:
        bool: whether string is palindrome
    """
    pass

# s = "madam"
# is_palindrome(s)

# s = "madamweb"
# is_palindrome(s)


# Problem 3: Squash Spaces
def squash_spaces(s: str) -> str:
    """
    Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.

    Parameters:
        s (str): string

    Returns:
        str: string with each substring with consecutive spaces reduced to single space
    """
    pass

# s = "   Up,     up,   and  away! "
# squash_spaces(s)

# s = "With great power comes great responsibility."
# squash_spaces(s)


# Problem 4: Two-Pointer Two Sum
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Use the two pointer approach to implement a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

    Parameters:
        nums (list[int]): sorted list of integers
        target (int): target integer

    Returns:
        list[int]: indices of two numbers that add up to target
    """
    pass

# nums = [2, 7, 11, 15]
# target = 9
# two_sum(nums, target)

# nums = [2, 7, 11, 15]
# target = 18
# two_sum(nums, target)


# Problem 5: Three Sum
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Parameters:
        nums (list[int]): integer array

    Returns:
        list[list[int]]: all triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
    """
    pass

# nums = [-1, 0, 1, 2, -1, -4]
# three_sum(nums)

# nums = [0, 1, 1]
# three_sum(nums)

# nums = [0, 0, 0]
# three_sum(nums)


# Problem 6: Insert Interval
def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.
    Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Return intervals after the insertion.
    You don't need to modify intervals in-place. You can make a new array and return it.
    
    Parameters:
        intervals (list[list[int]]): non-overlapping intervals where intervals[i] = [starti, endi] represent start and end of ith interval and sorted in ascending order by starti
        new_interval (list[int]): interval that represents start and end of another interval

    Returns:
        list[list[int]]: intervals after insertion
    """
    pass

# intervals = [[1, 3], [6, 9]]
# new_interval = [2, 5]
# insert_interval(intervals, new_interval)

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# new_interval = [4, 8]
# insert_interval(intervals, new_interval)