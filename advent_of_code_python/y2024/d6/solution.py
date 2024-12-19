import sys
from enum import Enum
from pathlib import Path

class Directions(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def next(self) -> Enum:
        match self:
            case Directions.UP:
                return Directions.RIGHT
            case Directions.RIGHT:
                return Directions.DOWN
            case Directions.DOWN:
                return Directions.LEFT
            case Directions.LEFT:
                return Directions.UP

class Solution:
    
    def __init__(self, file_name):
        self.map = []
        self.cur_i = 0
        self.cur_j = 0

        with open(Path(__file__).parent / file_name , 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                for j, char in enumerate(line):
                    if char == '^':
                        self.cur_i = i
                        self.cur_j = j
                self.map.append(list(line.strip()))

    def solve_part_one(self) -> int:
        is_in_map = True
        distinct_positions_walked = 0
        curr_direction = Directions.UP

        while (is_in_map):
            next_i = self.cur_i + curr_direction.value[1]
            next_j = self.cur_j + curr_direction.value[0]
            
            if (next_i < 0 or next_i >= len(self.map) or next_j < 0 or next_j >= len(self.map[0])):
                distinct_positions_walked += 1
                self.map[self.cur_i][self.cur_j] = 'X'
                self.cur_i = next_i
                self.cur_j = next_j
                is_in_map = False
            elif self.map[next_i][next_j] == '#':
               curr_direction = curr_direction.next()
            else:
                if self.map[self.cur_i][self.cur_j] == '.' or self.map[self.cur_i][self.cur_j] == '^':
                    distinct_positions_walked += 1

                self.map[self.cur_i][self.cur_j] = 'X'
                self.cur_i = next_i
                self.cur_j = next_j
            
        return distinct_positions_walked
    
    def solve_part_two(self) -> int :
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