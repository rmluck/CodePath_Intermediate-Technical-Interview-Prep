"""
Problem Set 2.1
"""

import string


## ADVANCED PROBLEM SET VERSION 1

# Problem 1: Counting Treasure
def total_treasure(treasure_map: dict) -> int:
    """
    Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

    Parameters:
        treasure_map (dict): dictionary in which keys are location names and values are integers representing number of treasures buried at those locations

    Returns:
        int: total number of treasures buried on island
    """

    treasures = 0
    
    for value in treasure_map.values():
        treasures += value

    return treasures

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasure(treasure_map1))
# print(total_treasure(treasure_map2))


# Problem 2: Pirate Message Check
def can_trust_message(message: str) -> bool:
    """
    Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

    Parameters:
        message (str): string containing only lowercase English letters and whitespace

    Returns:
        bool: whether message contains every letter of English alphabet at least once
    """
    
    letters_found = set()

    for char in message:
        if char != " ":
            letters_found.add(char)
    
    return len(letters_found) == 26

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))


# Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests: list[int]) -> list[int]:
    """
    Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

    Parameters:
        chests (list[int]): integer array of length n where all integers are in range [1, n] and each integer appears once or twice

    Returns:
        list[int]: array of all integers that appear twice, representing treasure chests that have duplicates
    """

    chests_found = set()
    duplicates = []
    
    for chest in chests:
        if chest in chests_found and chest not in duplicates:
            duplicates.append(chest)
        elif chest not in chests_found:
            chests_found.add(chest)
    
    return duplicates


# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))


# Problem 4: Booby Trap
def is_balanced(code: str) -> bool:
    """
    Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.
    Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

    Parameters:
        code (str): 0-indexed string consisting of only lowercase English letters

    Returns:
        bool: whether it is possible to remove one letter so that frequency of all remaining letters is equal
    """
    
    letters_found = {}

    for letter in code:
        if letter in letters_found:
            letters_found[letter] += 1
        else:
            letters_found[letter] = 1

    frequencies = set()

    for value in letters_found.values():
        frequencies.add(value)
    
    if len(frequencies) != 2:
        return False
    else:
        frequency_list = []
        for frequency in frequencies:
            frequency_list.append(frequency)
        
        return abs(frequency_list[0] - frequency_list[1]) == 1

# code1 = "arghh"
# code2 = "haha"
# code3 = "abcabcaaa"

# print(is_balanced(code1))
# print(is_balanced(code2))
# print(is_balanced(code3))


# Problem 5: Overflowing with Gold
def find_treasure_indices(gold_amounts: list[int], target: int) -> list[int]:
    """
    Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.
    Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.
    Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

    Parameters:
        gold_amounts (list[int]): array of integers representing amount of gold at each location
        target (int): integer representing target amount

    Returns:
        list[int]: indices of two locations whose gold amounts add up to target
    """
    
    for i in range(len(gold_amounts)):
        current_amount = target - gold_amounts[i]
        
        for j in range(len(gold_amounts)):
            if i != j and current_amount == gold_amounts[j]:
                return [i, j]


# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))
# print(find_treasure_indices(gold_amounts2, target2))
# print(find_treasure_indices(gold_amounts3, target3))


# Problem 6: Organize the Pirate Crew
def organize_pirate_crew(group_sizes: list[int]) -> list[int]:
    """
    Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.
    You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.
    Return a list of groups such that each pirate i is in a group of size group_sizes[i].
    Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

    Parameters:
        group_sizes (list[int]): integer array where group_sizes[i] is size of group that pirate i should be in

    Returns:
        list[int]: list of groups such that each pirate i is in group of size groups_size[i]
    """
    
    sizes = {}
    groups = []

    for i in range(len(group_sizes)):
        size = group_sizes[i]
        if size in sizes:
            sizes[size].append(i)
        else:
            sizes[size] = [i]
        
        if len(sizes[size]) == size:
            groups.append(sizes[size])
            sizes[size] = []    
    
    return groups
    
# group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
# group_sizes2 = [2, 1, 3, 3, 3, 2]

# print(organize_pirate_crew(group_sizes1))
# print(organize_pirate_crew(group_sizes2)) 


def min_steps_to_match_maps(map1: str, map2: str) -> int:
    """
    Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.
    Return the minimum number of steps to make map2 an anagram of map1.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

    Parameters:
        map1 (str): string representing treasure map
        map2 (str): string representing treasure map

    Returns:
        int: minimum number of steps to make map 2 an anagram of map1
    """
    
    for letter in map2:
        if letter in map1:
            map1 = map1.replace(letter, "", 1)
    
    return len(map1)

# map1_1 = "bab"
# map2_1 = "aba"
# map1_2 = "treasure"
# map2_2 = "huntgold"
# map1_3 = "anagram"
# map2_3 = "mangaar"

# print(min_steps_to_match_maps(map1_1, map2_1))
# print(min_steps_to_match_maps(map1_2, map2_2))
# print(min_steps_to_match_maps(map1_3, map2_3))


# Problem 8: Counting Pirates' Action Minutes
def counting_pirates_action_minutes(log: list[int], k: int) -> list[int]:
    """
    Captain Dread is keeping track of the crew's activities using a log. The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] indicates that the pirate with pirateID performed an action at the minute time.
    Multiple pirates can perform actions simultaneously, and a single pirate can perform multiple actions in the same minute.
    The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate performed an action. A minute can only be counted once, even if multiple actions occur during it.
    You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.
    Return the array answer as described above.

    Parameters:
        log (list[int]): 2D integer array where each logs[i] = [pirateID, time] indicates that pirate with pirateID performed action at minute time
        k (int): size of log

    Returns:
        list[int]: 1-indexed array of size k such that for each j (1 <= j <= k), answer[j] is number of pirates whose PAM equals j
    """
    pass

# logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
# k1 = 5
# logs2 = [[1, 1], [2, 2], [2, 3]]
# k2 = 4

# print(counting_pirates_action_minutes(logs1, k1)) 
# print(counting_pirates_action_minutes(logs2, k2))


## ADVANCED PROBLEM SET VERSION 2

# Problem 1: The Library of Alexandria
def analyze_library(library_catalog: dict, actual_distribution: dict) -> dict:
    """
    In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. You are given a dictionary library_catalog that maps room names to the number of scrolls that room should have and a second dictionary actual_distribution that maps room names to the number of scrolls found in that room after the temporal rift.
    Write a function analyze_library() that determines if any room has more or fewer scrolls than it should. The function should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls (actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences.

    Parameters:
        library_catalog (dict): dictionary that maps room names to number of scrolls that room should have
        actual_distribution (dict): dictionary that maps room names to number of scrolls found in that room after temporal rift

    Returns:
        dict: dictionary where keys are room names and values are differences in number of scrolls (actual number of scrolls - expected number of scrolls)
    """

    differences = {}

    for key in library_catalog.keys():
        differences[key] = actual_distribution[key] - library_catalog[key]
    
    return differences

# library_catalog = {
#     "Room A": 150,
#     "Room B": 200,
#     "Room C": 250,
#     "Room D": 300
# }

# actual_distribution = {
#     "Room A": 150,
#     "Room B": 190,
#     "Room C": 260,
#     "Room D": 300
# }

# print(analyze_library(library_catalog, actual_distribution))


# Problem 2: Grecian Artifacts
def find_common_artifacts(artifacts1: list[str], artifacts2: list[str]) -> list[str]:
    """
    You've spent your last few trips exploring different periods of Ancient Greece. During your travels, you discover several interesting artifacts. Some artifacts appear in multiple time periods, while others in just one.
    You are given two lists of strings artifacts1 and artifacts2 representing the artifacts found in two different time periods. Write a function find_common_artifacts() that returns a list of artifacts common to both time periods.

    Parameters:
        artifacts1 (list[str]): list of strings representing artifacts found in one time period
        artifacts2 (list[str]): list of strings representing artifacts found in another time period

    Returns:
        list[str]: list of artifacts common to both time periods
    """
    
    common_artifacts = []

    for artifact in artifacts1:
        if artifact in artifacts2:
            common_artifacts.append(artifact)
    
    return common_artifacts

# artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
# artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

# print(find_common_artifacts(artifacts1, artifacts2))


# Problem 3: Souvenir Declutter
def declutter(souvenirs: list[str], threshold: int) -> list[str]:
    """
    As a time traveler, you've collected a mountain of souvenirs over the course of your travels. You're running out of room to store them all and need to declutter. Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter() that returns a list of souvenirs strictly below threshold.

    Parameters:
        souvenirs (list[str]): list of strings
        threshold (int): integer representing threshold for souvenirs

    Returns:
        list[str]: list of souvenirs strictly below threshold
    """
    
    frequencies = {}
    decluttered_souvenirs = []

    for souvenir in souvenirs:
        if souvenir in frequencies:
            frequencies[souvenir] += 1
        else:
            frequencies[souvenir] = 1
    
    for key, value in frequencies.items():
        if value < threshold:
            for v in range(value):
                decluttered_souvenirs.append(key)

    return decluttered_souvenirs

# souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
# threshold1 = 3

# souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
# threshold2 = 2

# print(declutter(souvenirs1, threshold1))
# print(declutter(souvenirs2, threshold2))


# Problem 4: Time Portals
def num_of_time_portals(portals: list[str], destination: str) -> int:
    """
    In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.
    Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

    Parameters:
        portals (list[str]): array of digit strings
        destination (str): digit string

    Returns:
        int: number of pairs of indices (i, j) (where i != j) such that concatenation of portals[i] + portals[j] equals destination
    """
    
    num_pairs = 0

    for i in range(len(portals)):
        for j in range(len(portals)):
            if i != j and portals[i] + portals[j] == destination:
                num_pairs += 1
    
    return num_pairs

# portals1 = ["777", "7", "77", "77"]
# destination1 = "7777"
# portals2 = ["123", "4", "12", "34"]
# destination2 = "1234"
# portals3 = ["1", "1", "1"]
# destination3 = "11"

# print(num_of_time_portals(portals1, destination1))
# print(num_of_time_portals(portals2, destination2))
# print(num_of_time_portals(portals3, destination3))


# Problem 5: Detect Temporal Anomaly
def detect_temporal_anomaly(time_points: list[int], k: int) -> bool:
    """
    As a time traveler, you have recorded the occurrences of specific events at different time points. You suspect that some events might be occurring too frequently within short time spans, indicating potential temporal anomalies. Given an array time_points where each element represents an event ID at a particular time point, and an integer k, determine if there are two distinct time points i and j such that time_points[i] == time_points[j] and the absolute difference between i and j is at most k.
    Note: The indices must be unique, but not the values i and j themselves.

    Parameters:
        time_points (list[int]): array where each element represents event ID at particular time point
        k (int): integer

    Returns:
        bool: whether there are two distinct time points i and j such that time_points[i] == time_points[j] and absolute difference between i and j is at most k
    """
    
    for i in range(len(time_points)):
        for j in range(len(time_points)):
            if i != j and time_points[i] == time_points[j] and abs(i - j) <= k:
                return True
    
    return False

# time_points1 = [1, 2, 3, 1]
# k1 = 3

# time_points2 = [1, 0, 1, 1]
# k2 = 1

# time_points3 = [1, 2, 3, 1, 2, 3]
# k3 = 2

# print(detect_temporal_anomaly(time_points1, k1)) 
# print(detect_temporal_anomaly(time_points2, k2))
# print(detect_temporal_anomaly(time_points3, k3))


# Problem 6: Find Travelers with Zero or One Temporal Anomalies
def find_travelers(anomalies: list[int]) -> list[list[int]]:
    """
    In your time travel adventures, you are given an integer array anomalies where anomalies[i] = [traveleri, anomalyi] indicates that the traveler traveleri caused a temporal anomaly anomalyi.
    Return a list answer of size 2 where:
    - answer[0] is a list of all travelers that have not caused any anomalies
    - answer[1] is a list of all travelers that have caused exactly one anomaly
    The values in the two lists should be returned in increasing order.
    Note: You should only consider the travelers that have experienced at least one anomaly.

    Parameters:
        anomalies (list[int]): integer array where anomalies[i] = [traveleri, anomalyi] indicates that traveler traveleri caused temporal anomaly anomalyi

    Returns:
        list[list[int]]: list of size 2 where answer[0] is list of all travelers that have not caused any anomalies and answer[1] is list of all travelers that have caused exactly one anomaly
    """
    pass

# anomalies1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# anomalies2 = [[2,3],[1,3],[5,4],[6,4]]

# print(find_travelers(anomalies1)) 
# print(find_travelers(anomalies2))


# Problem 7: Lingual Frequencies
def find_most_frequent_word(text: str, illegibles: list[str]) -> str:
    """
    As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in the text are illegible and can't be deciphered. Write a function find_most_frequent_word() that accepts a string text and a list of illegible words illegibles and returns the most frequent word in text that is not an illegible word.

    Parameters:
        text (str): string
        illegibles (list[str]): list of illegible words

    Returns:
        str: most frequent word in text that is not illegible word
    """
    
    frequencies = {}

    text = text.lower()
    text = "".join(l for l in text if l not in string.punctuation)
    for word in text.split():
        if word not in illegibles:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
    
    max_string = None
    max_val = float("-inf")
    for key, value in frequencies.items():
        if value > max_val:
            max_string = key
            max_val = value
    
    return max_string

# paragraph1 = "a."
# illegibles1 = []
# print(find_most_frequent_word(paragraph1, illegibles1)) 

# paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
# illegibles2 = ["hit"]
# print(find_most_frequent_word(paragraph2, illegibles2))


# Problem 8: Time Portal Usage
def display_time_portal_usage(usage_records: list[list[str]]) -> list[list[str]]:
    """
    In your time travel adventures, you have been collecting data on the usage of different time portals by various travelers. The data is represented by an array usage_records, where usage_records[i] = [traveler_name, portal_number, time_used] indicates that the traveler traveler_name used the portal portal_number at the time time_used.
    Return the adventure's "display table". The "display table" is a table whose row entries denote how many times each portal was used at each specific time. The first column is the portal number and the remaining columns correspond to each unique time in chronological order. The first row should be a header whose first column is "Portal", followed by the times in chronological order. Note that the traveler names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

    Parameters:
        usage_records (list[list[str]]): array where usage_records[i] = [traveler_name, portal_number, time_used] indicates that traveler traveler_name used portal portal_number at time time_used
    """
    pass

# usage_records1 = [["David","3","10:00"],
#                   ["Corina","10","10:15"],
#                   ["David","3","10:30"],
#                   ["Carla","5","11:00"],
#                   ["Carla","5","10:00"],
#                   ["Rous","3","10:00"]]
# usage_records2 = [["James","12","11:00"],
#                   ["Ratesh","12","11:00"],
#                   ["Amadeus","12","11:00"],
#                   ["Adam","1","09:00"],
#                   ["Brianna","1","09:00"]]
# usage_records3 = [["Laura","2","08:00"],
#                   ["Jhon","2","08:15"],
#                   ["Melissa","2","08:30"]]

# print(display_time_portal_usage(usage_records1))
# print(display_time_portal_usage(usage_records2))
# print(display_time_portal_usage(usage_records3))