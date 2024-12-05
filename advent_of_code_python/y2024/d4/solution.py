from enum import Enum
from pathlib import Path
from typing import List
import sys

class Directions(Enum):
    RIGHT = (1, 0)
    BOTTOM_RIGHT = (1, 1)
    DOWN = (0, 1)
    BOTTOM_LEFT = (-1, 1)
    LEFT = (-1, 0)
    UPPER_LEFT = (-1, -1)
    UP = (0, -1)
    UPPER_RIGHT = (1, -1)

class Solution:
     
    def __init__(self, file_name):
        self.word_search = []

        with open(Path(__file__).parent / file_name , 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.word_search.append(line.splitlines()[0])
    
    # Idea: Search the grid. If x is found, conduct search in all directions. If matched, then add +2
    def solve_part_one(self):
        total_valid_xmas_instances = 0
              
        for i in range(len(self.word_search)):
            for j in range(len(self.word_search[0])):
                current_char = self.word_search[i][j]
                if current_char == 'X':
                    total_valid_xmas_instances += self.search_xmas(i, j, self.word_search)
            
        return total_valid_xmas_instances
    
    def solve_part_two(self):
        return 0
    
    def search_xmas(self, row: int, column: int, word_search: List[List[int]]) -> int:
        valid_xmas_instances = 0
        max_row_len = len(word_search)
        max_column_len = len(word_search[0])

        for direction in Directions:
            xmas_capture = ''
            x_direction = direction.value[0]
            y_direction = direction.value[1]

            for i in range(0,4):
                cur_x = column + (i * x_direction)
                cur_y = row + (i * y_direction)

                if x_direction > 0:
                    if cur_x >= max_column_len:
                        break
                else:
                    if cur_x < 0:
                        break
                if y_direction > 0:
                    if cur_y >= max_row_len:
                        break
                else:
                    if cur_y < 0:
                        break

                xmas_capture += word_search[cur_y][cur_x]
            if xmas_capture == 'XMAS':
                valid_xmas_instances += 1
        
        return valid_xmas_instances
                


def main():
    solution = Solution(sys.argv[1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

    return

if __name__ == "__main__":
    main()