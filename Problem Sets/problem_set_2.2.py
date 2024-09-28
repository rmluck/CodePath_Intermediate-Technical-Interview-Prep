"""
Problem Set 2.2
"""


## ADVANCED PROBLEM SET VERSION 1

# Problem 1: Balanced Art Collection
def find_balanced_subsequence(art_pieces: list[int]) -> int:
    """
    As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.
    Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.
    A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

    Parameters:
        art_pieces (list[int]): integer array representing value of each art piece

    Returns:
        int: length of longest balanced subsequence
    """
    
    art_pieces = sorted(art_pieces)

    count = {}
    for piece in art_pieces:
        if piece in count:
            count[piece] += 1
        else:
            count[piece] = 1
    
    maximum = 0
    for piece in count.keys():
        if piece - 1 in count and count[piece] + count[piece - 1] > maximum:
            maximum = count[piece] + count[piece - 1]
        if piece + 1 in count and count[piece] + count[piece + 1] > maximum:
            maximum = count[piece] + count[piece + 1]
    
    return maximum

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))


# Problem 2: Verifying Authenticity
def is_authentic_collection(art_pieces: list[int]) -> bool:
    """
    Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].
    The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].
    Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.
    Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

    Parameters:
        art_pieces (list[int]): array of integers representing value of each art piece

    Returns:
        bool: whether art_pieces is authentic array
    """
    
    n = max(art_pieces)

    count = {}
    for piece in art_pieces:
        if piece in count:
            count[piece] += 1
        else:
            count[piece] = 1
    
    for i in range(1, n):
        if count[i] != 1:
            return False
    
    if count[n] == 2:
        return True
    else:
        return False

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))


# Problem 3: Gallery Wall
def organize_exhibition(collection: list[str]) -> list[list[str]]:
    """
    You are tasked with organizing a collection of art prints represented by a list of strings collection. You need to display these prints on a single wall in a 2D array format that meets the following criteria:
    1. The 2D array should contain only the elements of the array collection.
    2. Each row in the 2D array should contain distinct strings.
    3. The number of rows in the 2D array should be minimal.
    Return the resulting array. If there are multiple answers, return any of them. Note that the 2D array can have a different number of elements on each row.

    Parameters:
        collection (list[str]): collection of art prints

    Returns:
        list[list[str]]: 2D array of art prints on single wall
    """
    
    count = {}
    for print in collection:
        if print in count:
            count[print] += 1
        else:
            count[print] = 1
    
    wall = []
    for i in range(1, max(count.values()) + 1):
        row = []
        for print in count.keys():
            if count[print] >= i:
                row.append(print)
        wall.append(row)
    
    return wall

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
#               "Kahlo", "O'Keefe"]
# collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))


# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains: list[str]) -> list[str]:
    """
    Your gallery has been trying to increase it's online presence by hosting several virtual galleries. Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.
    A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "artmuseum.com", and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", they also implicitly visit the parent domains "artmuseum.com" and "com".
    A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
    - For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
    Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.

    Parameters:
        cpdomains (list[str]): list of count-paired domains

    Returns:
        list[str]: list of count-paired domains of each subdomain
    """
    
    count = {}
    for site in cpdomains:
        n, site = site.split(" ")
        site = site.split(".")
        for i in range(len(site)):
            subdomain = ".".join(site[i:])
            if subdomain in count:
                count[subdomain] += int(n)
            else:
                count[subdomain] = int(n)
    
    domains = []
    for key, val in count.items():
        domains.append(f"{val} {key}")

    return domains

# cpdomains1 = ["9001 modern.artmuseum.com"]
# cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
#               "1 contemporary.gallery.com", "5 medieval.org"]

# print(subdomain_visits(cpdomains1))
# print(subdomain_visits(cpdomains2))


# Problem 5: Beautiful Collection
def beauty_sum(collection: str) -> int:
    """
    Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string collection where each artist in your gallery is represented by a character. The beauty of a collection is defined as the difference in frequencies between the most frequent and least frequent characters.
    - For example, the beauty of "abaacc" is 3 - 1 = 2.
    Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its substrings (subcollections), not just of the collection itself.

    Parameters:
        collection (str): string representing collection

    Returns:
        int: sum of beauty of all subcollections
    """
    pass

# print(beauty_sum("aabcb")) 
# print(beauty_sum("aabcbaa"))


# Problem 6: Counting Divisible Collections in the Gallery
def count_divisible_collections(collection_sizes: list[int], k: int) -> int:
    """
    You have a list of integers collection_sizes representing the sizes of different art collections in your gallery and are trying to determine how to group them to best fit in your space. Given an integer k write a function count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the array) where the sum of the sizes is divisible by k.

    Parameters:
        collection_sizes (list[int]): list of integers representing sizes of different art collections in gallery
        k (int): integer that sum of sizes should be divisible by

    Returns:
        int: number of non-empty subarrays where sum of sizes is divisible by k
    """
    pass

# nums1 = [4, 5, 0, -2, -3, 1]
# k1 = 5
# nums2 = [5]
# k2 = 9

# print(count_divisible_collections(nums1, k1)) 
# print(count_divisible_collections(nums2, k2))


# ADVANCED PROBLEM SET VERSION 2

# Problem 1: Cook Off
from collections import Counter

def max_attempts(ingredients: str, target_meal: str) -> int:
    """
    In a reality TV show, contestants are challenged to do the best recreation of a meal cooked by an all-star judge using limited resources. The meal they must recreate is represented by the string target_meal. The contestants are given a collection of ingredients represented by the string ingredients.
    Help the contestants by writing a function max_attempts() that returns the maximum number of copies of target_meal they can create using the given ingredients. You can take some letters from ingredients and rearrange them to form new strings.

    Parameters:
        ingredients (str): collection of ingredients
        target_meal (str): meal that must be recreated

    Returns:
        int: maximum number of copies of target_meal that can be created using given ingredients
    """

    ingredients_count = Counter(ingredients)
    target_count = Counter(target_meal)

    attempts = float("inf")
    for letter in target_count:
        if letter not in ingredients_count:
            return 0
        
        attempts = min(attempts, ingredients_count[letter] // target_count[letter])

    return attempts

# ingredients1 = "aabbbcccc"
# target_meal1 = "abc"

# ingredients2 = "ppppqqqrrr"
# target_meal2 = "pqr"

# ingredients3 = "ingredientsforcooking"
# target_meal3 = "cooking"

# print(max_attempts(ingredients1, target_meal1))
# print(max_attempts(ingredients2, target_meal2))
# print(max_attempts(ingredients3, target_meal3))


# Problem 2: Dialogue Similarity
def is_similar(sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]) -> bool:
    """
    Watching a reality TV show, you notice a lot of contestants talk similarly. We want to determine if two contestants have similar speech patterns.
    We can represent a sentence as an array of words, for example, the sentence "I've got a text!" can be represented as sentence = ["I've", "got", "a", "text"].
    You are given two sentences from different contestants sentence1 and sentence2 each represented as a string array and given an array of string pairs similar_pairs where similar_pairs[i] = [xi, yi] indicates that the two words xi and yi are similar. Write a function is_similar() that returns True if sentence1 and sentence2 are similar, and False if they are not similar.
    Two sentences are similar if:
    - They have the same length (i.e., the same number of words)
    - sentence1[i] and sentence2[i] are similar
    Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.

    Parameters:
        sentence1 (list[str]): sentence with contestants
        sentence2 (list[str]): sentence with contestants
        similar_pairs (list[list[str]]): array of string pairs where similar_pairs[i] = [xi, yi] indicates that two words xi and yi are similar
        
    Returns:
        bool: whether sentence1 and sentence2 are similar
    """
    
    if len(sentence1) != len(sentence2):
        return False
    
    for i in range(len(sentence1)):
        if sentence1[i] != sentence2[i] and [sentence1[i], sentence2[i]] not in similar_pairs:
            return False
    
    return True


# sentence1 = ["my", "type", "on", "paper"]
# sentence2 = ["my", "type", "in", "theory"]
# similar_pairs = [ ["on", "in"], ["paper", "theory"]]

# sentence3 = ["no", "tea", "no", "shade"]
# sentence4 = ["no", "offense"]
# similar_pairs2 = [["shade", "offense"]]

# print(is_similar(sentence1, sentence2, similar_pairs))
# print(is_similar(sentence3, sentence4, similar_pairs2))


# Problem 3: Cows and Bulls
def get_hint(secret: str, guess: str) -> str:
    """
    In a reality TV show, contestants play a mini-game called Bulls and Cows for a prize. The objective is to guess a secret number within a limited number of attempts. You, as the host, need to provide hints to the contestants based on their guesses.
    When a contestant makes a guess, you provide a hint with the following information:
    - The number of "bulls," which are digits in the guess that are in the correct position.
    - The number of "cows," which are digits in the guess that are in the secret number but are located in the wrong position.
    Given the secret number secret and the contestant's guess guess, return the hint for their guess.
    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

    Parameters:
        secret (str): secret number
        guess (str): contestant's guess

    Returns:
        str: hint for guess
    """

    count = {}
    for num in secret:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    bulls, cows = 0, 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            bulls += 1
            count[secret[i]] -= 1
        elif guess[i] in count and count[guess[i]] > 0:
            cows += 1
            count[guess[i]] -= 1
    
    return f"{bulls}A{cows}B"

# secret1 = "1807"
# guess1 = "7810"

# secret2 = "1123"
# guess2 = "0111"

# print(get_hint(secret1, guess1))
# print(get_hint(secret2, guess2))


# Problem 4: Count Winning Pairings
def count_winning_pairings(star_power: list[int]) -> int:
    """
    In a popular reality TV show, contestants pair up for various challenges. The pairing is considered winning if the sum of their "star power" is a power of two.
    You are given an array of integers star_power where star_power[i] represents the star power of the i-th contestant. Return the number of different winning pairings you can make from this list, modulo 10^9 + 7.
    Note that contestants with different indices are considered different even if they have the same star power.
    
    Parameters:
        star_power (list[int]): array of integers where star_power[i] represents star power of i-th contestant

    Returns:
        int: number of different winning pairings that can be made from list, modulo 10^9 + 7
    """
    pass

# star_power1 = [1, 3, 5, 7, 9]
# print(count_winning_pairings(star_power1))

# star_power2 = [1, 1, 1, 3, 3, 3, 7]
# print(count_winning_pairings(star_power2))


# Problem 5: Assigning Unique Nicknames to Contestants
def assign_unique_nicknames(nicknames: list[str]) -> list[str]:
    """
    In a reality TV show, contestants are assigned unique nicknames. However, two contestants cannot have the same nickname. If a contestant requests a nickname that has already been taken, the show will add a suffix to the name in the form of (k), where k is the smallest positive integer that makes the nickname unique.
    You are given an array of strings nicknames representing the requested nicknames for the contestants. Return an array of strings where result[i] is the actual nickname assigned to the ith contestant.
    
    Parameters:
        nicknames (list[str]): list of strings representing requested nicknames for contestants

    Returns:
        list[str]: array of strings where result[i] is actual nickname assigned to i-th contestant
    """
    
    new_nicknames = []
    count = {}

    for nickname in nicknames:
        if nickname in count:
            new_nicknames.append(f"{nickname}({count[nickname]})")
            count[nickname] += 1
        else:
            count[nickname] = 1
            new_nicknames.append(nickname)
    
    return new_nicknames

# nicknames1 = ["Champ","Diva","Champ","Ace"]
# print(assign_unique_nicknames(nicknames1))

# nicknames2 = ["Ace","Ace","Ace","Maverick"]
# print(assign_unique_nicknames(nicknames2)) 

# nicknames3 = ["Star","Star","Star","Star","Star"]
# print(assign_unique_nicknames(nicknames3))


# Problem 6: Pair Contestants
def pair_contestants(scores: list[int], k: int) -> bool:
    """
    In a reality TV challenge, contestants must be paired up in teams. Each team's combined score must be divisible by a target number k. You are given an array of integers scores representing the scores of the contestants and an integer k.
    You need to determine whether it is possible to pair all contestants such that the sum of the scores of each pair is divisible by k.
    Return True if it is possible to form the required pairs, otherwise return False.
    
    Parameters:
        scores (list[int]): array of integers representing scores of contestants
        k (int): target number

    Returns:
        bool: whether it is possible to form required pairs
    """
    pass

# scores1 = [1,2,3,4,5,10,6,7,8,9]
# k1 = 5
# print(pair_contestants(scores1, k1))

# scores2 = [1,2,3,4,5,6]
# k2 = 7
# print(pair_contestants(scores2, k2))

# scores3 = [1,2,3,4,5,6]
# k3 = 10
# print(pair_contestants(scores3, k3))
