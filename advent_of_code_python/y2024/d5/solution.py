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
    # once, make the value into a list.
    # Time: O(n^2). Space: O(n)
    def solve_part_one(self) -> int:
        sum_of_correctly_ordered_updates = 0

        for page_update in self.page_updates:
            sum_of_correctly_ordered_updates += self.midpoint_for_valid_page_updates(page_update)

        return sum_of_correctly_ordered_updates
    
    def solve_part_two(self):
        return 0
    
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
        
def main():
    solution = Solution(sys.argv[1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

    return

if __name__ == "__main__":
    main()