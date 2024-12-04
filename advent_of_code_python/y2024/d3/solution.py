import sys
import re
from pathlib import Path

class Solution:
    def __init__(self, file_name):
        with open(Path(__file__).parent / file_name , 'r') as file:
            self.corrupted_memory = file.read()

    # Idea: RegEx. Depends on implementation. Assuming using a finite state machine.
    def solve_part_one(self) -> int:
        return self.calculate_sum_of_instructions(self.corrupted_memory)
    
    # Idea: Split memory into "do" groups and "don't" groups. Only parse "do".
    def solve_part_two(self) -> int:
        sum_of_instructions = 0
        do_groups = self.corrupted_memory.split("do()")
        valid_groups = list(map(lambda g: g.split("don't()")[0], do_groups))
        for group in valid_groups:
            sum_of_instructions += self.calculate_sum_of_instructions(group)

        return sum_of_instructions
    
    def calculate_sum_of_instructions(self, input: str) -> int:
        sum_of_instructions = 0
        valid_instruction_pairs = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', input)
        for x,y in valid_instruction_pairs:
            sum_of_instructions += int(x) * int(y)

        return sum_of_instructions

def main():
    solution = Solution(sys.argv[1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

if __name__ == '__main__':
    main()