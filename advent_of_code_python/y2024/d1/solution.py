import sys
from pathlib import Path

class Solution:

    def __init__(self, file_name):
        self.left_list = []
        self.right_list = []

        with open(Path(__file__).parent / file_name , 'r') as file:
            lines = file.readlines()

            for line in lines:
                split_line = line.split()
                self.left_list.append(int(split_line[0]))
                self.right_list.append(int(split_line[1]))


    # Idea: Sort both lines.
    # Time: O(2nlogn) + O(n)
    # Space: O(1)
    def solve_part_one(self):
        total_diff = 0
        self.left_list.sort()
        self.right_list.sort()

        for i, number in enumerate(self.left_list):
            total_diff += abs(number - self.right_list[i])

        return total_diff
    
    # Idea: Left list does not need to be sorted. Second list can utilize a frequency count with a hashmap.
    # Time: O(2n)
    # Space: O(n)
    def solve_part_two(self):
        similarity_score = 0
        frequency_counter = {}
        
        for number in self.right_list:
            if number not in frequency_counter:
                frequency_counter[number] = 1
            else:
                frequency_counter[number] = frequency_counter[number] + 1
        
        for number in self.left_list:
            if number not in frequency_counter:
                continue
            else:
                similarity_score += number * frequency_counter[number]

        return similarity_score

    
def main():
    solution = Solution(sys.argv[-1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

if __name__ == '__main__':
    main()