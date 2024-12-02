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


    # Idea: Sort both lines. This becomes O(2nlogn) + O(n) runtime with O(2n) space.
    def solve_part_one(self):
        total_diff = 0
        self.left_list.sort()
        self.right_list.sort()

        for i, number in enumerate(self.left_list):
            total_diff += abs(number - self.right_list[i])

        return total_diff
    
def main():
    solution = Solution(sys.argv[-1])
    part_one_value = solution.solve_part_one()
    print(f'Solution Part 1: {part_one_value}')

if __name__ == '__main__':
    main()