"""
Problem Set 1.1 - Standard Problem Set 2
"""


# Problem 1: Batman
def batman():
    """
    Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
    """

    print("I am vengeance. I am the night. I am Batman!")

# batman()


# Problem 2: Mad Libs
def madlib(verb: str):
    """
    Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".

    Parameters:
        verb (str): string
    """

    print(f"I have one power. I never {verb}. - Batman")

# verb = "give up"
# madlib(verb)

# verb = "nap"
# madlib(verb)


# Problem 3: Trilogy
def trilogy(year: int):
    """
    Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.
    Year    | Movie Title
    ----------------------------------
    2005    | "Batman Begins"
    2008    | "The Dark Knight"
    2012    | "The Dark Knight Rises"

    Parameters:
        year (int): release year
    """

    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")

# year = 2008
# trilogy(year)

# year = 1998
# trilogy(year)


# Problem 4: Last
def get_last(items: list[str]) -> str:
    """
    Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.

    Parameters:
        items (list[str]): list of items
    
    Returns:
        str: last item in list
    """

    if items == []:
        return None
    else:
        return items[-1]

# items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# print(get_last(items))

# items = []
# print(get_last(items))


# Problem 5: Concatenate
def concatenate(words: list[str]) -> str:
    """
    Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

    Parameters:
        words (list[str]): list of strings

    Returns:
        str: string that concatenates all elements in words
    """

    concatenated = ""
    for word in words:
        concatenated += word
    
    return concatenated

# words = ["vengeance", "darkness", "batman"]
# print(concatenate(words))

# words = []
# print(concatenate(words))


# Problem 6: Squared
def squared(numbers: list[int]) -> list[int]:
    """
    Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

    Parameters:
        numbers (list[int]): list of integers
    
    Returns:
        list[int]: squared list
    """

    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    
    return numbers

# numbers = [1, 2, 3]
# print(squared(numbers))


# Problem 7: NaNaNa Batman!
def nanana_batman(x: int):
    """
    Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

    Parameters:
        x (int): integer
    """

    if x == 0:
        print("batman!")
    else:
        na = ""
        for i in range(x):
            na += "na"
        print(na, "batman!")

# x = 6
# nanana_batman(x)

# x = 0
# nanana_batman(x)


# Problem 8: Find the Villain
def find_villain(crowd: list[str], villain: str) -> list[int]:
    """
    Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

    Parameters:
        crowd (list[str]): list of characters
        villain (str): name of villain
    
    Returns:
        list[int]: list of indices where villain is found hiding in crowd
    """

    indices = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            indices.append(i)
    
    return indices

# crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
# villain = 'The Joker'
# print(find_villain(crowd, villain))


# Problem 9: Odd
def get_odds(nums: list[int]) -> list[int]:
    """
    Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

    Parameters:
        nums (list[int]): list of integers

    Returns:
        list[int]: list of odd numbers in nums
    """

    odd_numbers = []
    for num in nums:
        if num % 2 == 1:
            odd_numbers.append(num)

    return odd_numbers

# nums = [1, 2, 3, 4]
# print(get_odds(nums))

# nums = [2, 4, 6, 8]
# print(get_odds(nums))


# Problem 10: Up and Down
def up_and_down(lst: list[int]) -> int:
    """
    Write a function a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.

    Parameters:
        lst (list[int]): list of integers

    Returns:
        int: number of odd numbers minus number of even numbers in list
    """

    even_numbers = 0
    odd_numbers = 0
    for num in lst:
        if num % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    
    return odd_numbers - even_numbers

# lst = [1, 2, 3]
# print(up_and_down(lst))

# lst = [1, 3, 5]
# print(up_and_down(lst))

# lst = [2, 4, 10, 2]
# print(up_and_down(lst))


# Problem 11: Running Sum
def running_sum(superhero_stats: list[int]) -> list[int]:
    """
    Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). You must modify the list in place; you may not create any new lists as part of your solution.

    Parameters:
        superhero_stats (list[int]): list of number of crimes Batman has stopped each month in Gotham City

    Returns:
        list[int]: running sum of number of crimes Batman has stopped in Gotham City
    """

    sum = 0
    for i in range(len(superhero_stats)):
        sum += superhero_stats[i]
        superhero_stats[i] = sum

    return superhero_stats

# superhero_stats = [1, 2, 3, 4]
# print(running_sum(superhero_stats))

# superhero_stats = [1, 1, 1, 1, 1]
# print(running_sum(superhero_stats))

# superhero_stats = [3, 1, 2, 10, 1]
# print(running_sum(superhero_stats))
