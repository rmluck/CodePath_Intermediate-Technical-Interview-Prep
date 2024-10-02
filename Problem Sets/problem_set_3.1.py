"""
Problem Set 3.1
"""


## ADVANCED PROBLEM SET VERSION 1
def arrange_guest_arrival_order(arrival_pattern: str) -> str:
    """
    You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.
    You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:
    - guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
    - If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
    - If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
    Return the lexicographically smallest possible string guest_order that meets the conditions.

    Parameters:
        arrival_pattern (str): 0-indexed string of length n, consisting of characters 'I' meaning next guest should have higher status than previous one and 'D' meaning next guest should have lower status than previous one

    Returns:
        str: lexicographically smallest possible string guest_order that meets conditions
    """
    n = len(arrival_pattern)
    guest_order = []
    stack = []

    i = 1
    for i in range(n):
        if arrival_pattern[i] == "I":
            guest_order.append(str(i + 1))
            i += 1

            while stack:
                guest_order.append(stack.pop())
        else:
            stack.append(str(i + 1))
            i += 1
    
    guest_order.append(str(i + 1))
    while stack:
        guest_order.append(stack.pop())

    return "".join(guest_order)

# print(arrange_guest_arrival_order("IIIDIDDD"))
# print(arrange_guest_arrival_order("DDD"))


# Problem 2: Reveal Attendee List in Order
from collections import deque
def reveal_attendee_list_in_order(attendees: list[int]) -> list[int]:
    """
    You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees. You need to arrange the attendees in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.
    The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:
    - Take the top registration number from the list, reveal it, and remove it from the list.
    - If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
    - If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
    Return an ordering of the registration numbers that would reveal the attendees in increasing order.

    Parameters:
        attendees (list[int]): list of unique registration numbers associated with attendees

    Returns:
        list[int]: ordering of registration numbers that would reveal attendees in increasing order
    """
    registration_numbers = []
    numbers = deque()
    for attendee in attendees:
        numbers.append(attendee)
    while numbers:
        registration_numbers.append(numbers.popleft())
        if numbers:
            numbers.append(numbers.popleft())
    
    return registration_numbers

# print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
# print(reveal_attendee_list_in_order([1,1000]))


# ADVANCED PROBLEM SET VERSION 2

# Problem 1: Extra Treats
