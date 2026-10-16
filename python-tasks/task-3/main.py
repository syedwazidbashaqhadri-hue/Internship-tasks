# Task 3: Test all functions imported from solutions.py

from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    maximum_consecutive_pair_sum,
    all_unique_pairs,
)


def show(question, example_input, result, extra_input, extra_result):
    print(f"\n{question}")
    print(f"Example input: {example_input}")
    print(f"Output: {result}")
    print(f"Additional test: {extra_input}")
    print(f"Additional output: {extra_result}")


show("Q1. Word frequency",
     "python is easy and python is powerful",
     word_frequency("python is easy and python is powerful"),
     "hi hi there",
     word_frequency("hi hi there"))

show("Q2. Character frequency",
     "banana", character_frequency("banana"),
     "hello", character_frequency("hello"))

show("Q3. First non-repeating character",
     "swiss", first_non_repeating_character("swiss"),
     "aabb", first_non_repeating_character("aabb"))

show("Q4. Anagrams",
     'listen, silent', are_anagrams("listen", "silent"),
     'hello, world', are_anagrams("hello", "world"))

show("Q5. First repeating character",
     "programming", first_repeating_character("programming"),
     "abcde", first_repeating_character("abcde"))

show("Q6. Move zeros to end",
     [0, 3, 0, 1, 2, 0, 4], move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]),
     [0, 0, 5, 6], move_zeros_to_end([0, 0, 5, 6]))

show("Q7. Second highest distinct number",
     [10, 20, 40, 30, 40, 20], second_highest_distinct([10, 20, 40, 30, 40, 20]),
     [7, 7, 3], second_highest_distinct([7, 7, 3]))

show("Q8. Remove duplicates preserving order",
     [4, 2, 4, 5, 2, 7, 5], remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]),
     ["a", "b", "a"], remove_duplicates_preserve_order(["a", "b", "a"]))

show("Q9. Missing number",
     "nums=[1, 2, 4, 5, 6], N=6", find_missing_number([1, 2, 4, 5, 6], 6),
     "nums=[1, 3, 4], N=4", find_missing_number([1, 3, 4], 4))

show("Q10. First two-sum pair",
     "nums=[2, 7, 11, 15], target=9", two_sum_first_pair([2, 7, 11, 15], 9),
     "nums=[1, 4, 6], target=10", two_sum_first_pair([1, 4, 6], 10))

show("Q11. Closest to zero",
     [-8, -3, 2, 5, -2], closest_to_zero([-8, -3, 2, 5, -2]),
     [-4, -1, 1, 3], closest_to_zero([-4, -1, 1, 3]))

show("Q12. Common elements",
     "list1=[1,2,3,4,5], list2=[3,4,5,6,7]",
     common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
     "list1=[2,2,3], list2=[2,3,4]",
     common_elements([2, 2, 3], [2, 3, 4]))

show("Q13. Rotate right",
     "nums=[1,2,3,4,5], K=2", rotate_right([1, 2, 3, 4, 5], 2),
     "nums=[1,2,3], K=4", rotate_right([1, 2, 3], 4))

show("Q14. Maximum consecutive pair sum",
     [4, 7, 2, 9, 5], maximum_consecutive_pair_sum([4, 7, 2, 9, 5]),
     [1, 10, 2], maximum_consecutive_pair_sum([1, 10, 2]))

show("Q15. All unique pairs",
     "nums=[2,4,3,5,7,8,1], target=9",
     all_unique_pairs([2, 4, 3, 5, 7, 8, 1], 9),
     "nums=[1,2,3], target=20",
     all_unique_pairs([1, 2, 3], 20))
