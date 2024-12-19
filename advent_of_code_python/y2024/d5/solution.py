import sys
from pathlib import Path
from typing import List

class Solution:

    def __init__(self, file_name):
        self.rules = {}
        self.page_updates = []

        with open(Path(__file__).parent / file_name , 'r') as file:
            lines = file.readlines()
            for line in lines:
                if '|' in line:
                    first_page, second_page = [int(x) for x in line.split('|')]
                    if first_page not in self.rules:
                        self.rules[first_page] = [second_page]
                    else:
                     self.rules[first_page].append(second_page)
                elif ',' in line:
                    pages_numbers = [int(x) for x in line.split(',')]
                    self.page_updates.append(pages_numbers)

    # Idea: Parse each page ordering rule and generate a map where
    # key is first element of the rule and value is the second element. If a key is present more 
    # once, make the value into a list. Iterate over the list and check for previous values if they
    # are present in the rules mapping.
    # Time: O(n^2). Space: O(n)
    def solve_part_one(self) -> int:
        sum_of_correctly_ordered_updates = 0

        for page_update in self.page_updates:
            sum_of_correctly_ordered_updates += self.midpoint_for_valid_page_updates(page_update)

        return sum_of_correctly_ordered_updates
    
    # Idea: Same as above, but only fix the list and account for incorrect mappings. We fix the list by
    # iterating over the list, and swapping the numbers at the current position until it is fixed.
    # Time: O(n^2). Space: O(n)
    def solve_part_two(self):
        sum_of_incorrect_updates = 0

        for page_update in self.page_updates:
            sum_of_incorrect_updates += self.midpoint_for_invalid_page_updates(page_update)

        return sum_of_incorrect_updates
    
    def midpoint_for_valid_page_updates(self, current_page_update: List[int]) -> int:
        previous_pages = []

        for page_number in current_page_update:
            if page_number in self.rules.keys():
                for previous_page in previous_pages:
                    if previous_page in self.rules[page_number]:
                        return 0
                
            previous_pages.append(page_number)
                
        midpoint = len(current_page_update) // 2
        return current_page_update[midpoint]
        
    
    def midpoint_for_invalid_page_updates(self, current_page_update: List[int]) -> int:
        is_invalid_page_update = False
        prev_page_index = 0
        curr_page_index = 1

        while (curr_page_index < len(current_page_update)):
            curr_page_number = current_page_update[curr_page_index]
            if curr_page_number in self.rules.keys():
                prev_page_number = current_page_update[prev_page_index]
                if prev_page_number in self.rules[curr_page_number]:
                    temp_number = current_page_update[curr_page_index]
                    current_page_update[curr_page_index] = current_page_update[prev_page_index]
                    current_page_update[prev_page_index] = temp_number
                    is_invalid_page_update = True

            curr_page_index += 1
            if (curr_page_index == len(current_page_update)):
                prev_page_index += 1
                curr_page_index = prev_page_index + 1    

        
        if (is_invalid_page_update):
            midpoint = len(current_page_update) // 2
            return current_page_update[midpoint]
        else:
            return 0
    
def main():
    solution = Solution(sys.argv[1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

    return

if __name__ == "__main__":
    main()