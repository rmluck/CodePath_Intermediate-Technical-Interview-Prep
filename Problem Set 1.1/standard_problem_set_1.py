"""
Problem Set 1.1 - Standard Problem Set 1
"""


# Problem 1: Hundred Acre Wood
def welcome():
    """
    Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
    """

    print("Welcome to The Hundred Acre Wood!")

# welcome()


# Problem 2: Greeting
def greeting(name: str):
    """
    Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin.".
    
    Parameters:
        name (str): name to be printed
    """

    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Michael")
# greeting("Winnie the Pooh")


# Problem 3: Catchphrase
def print_catchphrase(character: str):
    """
    Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below:
    CHARACTER           | CATCHPHRASE
    -----------------------------------------
    "Pooh"              | "Oh bother!"
    "Tigger"            | "TTFN: Ta-ta for now!"
    "Eeyore"            | "Thanks for noticing me."
    "Christopher Robin" | "Silly old bear."

    If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!".

    Parameters:
        character (str): name of character
    """

    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)


# Problem 4: Return Item
def get_item(items: list, x: int) -> str:
    """
    Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

    Parameters:
        items (list): list of items
        x (int): non-negative index
    
    Returns:
        str: item
    """

    if x < len(items):
        return items[x]
    else:
        return None

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))

# x = 5
# print(get_item(items, x))


# Problem 5: Total Honey
def sum_honey(hunny_jars: list[int]) -> int:
    """
    Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

    Parameters:
        hunny_jars (list[int]): list of integers
    
    Returns:
        int: sum of all elements in hunny_jars
    """
    
    honey_sum = 0
    for jar in hunny_jars:
        honey_sum += jar
    
    return honey_sum

# hunny_jars = [2, 3, 4, 5]
# print(sum_honey(hunny_jars))

# hunny_jars = []
# print(sum_honey(hunny_jars))


# Problem 6: Double Trouble
def doubled(hunny_jars: list[int]) -> list[int]:
    """
    Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

    Parameters:
        hunny_jars (list[int]): list of integers
    
    Returns:
        list[int]: doubled list
    """
    
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    
    return hunny_jars

# hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))


# Problem 7: Poohsticks
def count_less_than(race_times: list[int], threshold: int) -> int:
    """
    Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

    Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.
    
    Parameters:
        race_times (list[int]): list of race times
        threshold: race times threshold
    
    Returns:
        int: number of race times less than threshold
    """

    num_times = 0

    for time in race_times:
        if time < threshold:
            num_times += 1
    
    return num_times

# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# print(count_less_than(race_times, threshold))

# race_times = []
# threshold = 4
# print(count_less_than(race_times, threshold))


# Problem 8: Pooh's To Do's
def print_todo_list(task: list[str]):
    """
    Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:
    Pooh's To Dos:
    1. Task 1
    2. Task 2
    ...

    Parameters:
        task list[str]: list of tasks
    """

    for i in range(0, len(task)):
        print(f"{i + 1}. {task[i]}")

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)


# Problem 9: Pairs
def can_pair(item_quantities: list[int]) -> bool:
    """
    Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

    Parameters:
        item_quantities (list[int]): list of item quantities
    
    Returns:
        bool: whether each number in item_quantities is even
    """

    for num in item_quantities:
        if num % 2 == 1:
            return False
    
    return True

# item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

# item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

# item_quantities = []
# print(can_pair(item_quantities))


# Problem 10: Split Haycorns
def split_haycorns(quantity: int) -> list[int]:
    """
    Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.
    """

    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    
    return divisors

# quantity = 6
# print(split_haycorns(quantity))

# quantity = 1
# print(split_haycorns(quantity))


# Problem 11: T-I-Double Guh-ER
def tiggerfy(s: str) -> str:
    """
    Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

    Parameters:
        s (str): string
    
    Returns:
        str: new string with letters t, i, g, e, and r removed
    """

    new_string = ""
    for character in s:
        if character not in ["t", "i", "g", "e", "r", "T", "I", "G", "E", "R"]:
            new_string += character
    
    return new_string

# s = "suspicerous"
# print(tiggerfy(s))

# s = "Trigger"
# print(tiggerfy(s))

# s = "Hunny"
# print(tiggerfy(s))


# Problem 12: Thistle Hunt
def locate_thistles(items: list[str]) -> list[int]:
    """
    Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

    Parameters:
        items (list[str]): list of strings

    Returns:
        list[int]: list of indices of any elements with value "thistle"
    """

    indices = []
    for i in range(len(items)):
        if items[i] == "thistle":
            indices.append(i)
    
    return indices

# items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# print(locate_thistles(items))

# items = ["book", "bouncy ball", "leaf", "red balloon"]
# print(locate_thistles(items))
