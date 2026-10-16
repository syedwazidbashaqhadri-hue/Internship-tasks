# Task 3: Python Coding & Problem-Solving
# Each function returns a result instead of printing it.

# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    counts = {}
    for character in word:
        counts[character] = counts.get(character, 0) + 1
    return counts


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    counts = character_frequency(word)
    for character in word:
        if counts[character] == 1:
            return character
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return character_frequency(s1.replace(" ", "").lower()) == character_frequency(
        s2.replace(" ", "").lower()
    )


# Q5. Find the First Repeating Character in a String
def first_repeating_character(text):
    seen = set()
    for character in text:
        if character in seen:
            return character
        seen.add(character)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    non_zeros = [number for number in nums if number != 0]
    zeros = [number for number in nums if number == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(items):
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    seen = set()
    for number in nums:
        needed = target - number
        if needed in seen:
            # The earlier number is returned first.
            return [needed, number]
        seen.add(number)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums, key=lambda number: (abs(number), -number))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    second_set = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in second_set and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums.copy()
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def maximum_consecutive_pair_sum(nums):
    return max(nums[index] + nums[index + 1] for index in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
