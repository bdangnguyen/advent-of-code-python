import sys
from typing import List
from pathlib import Path

class Solution:
    
    def __init__(self, file_name):
        self.reports = []

        with open(Path(__file__).parent / file_name , 'r') as file:
            lines = file.readlines()

            for line in lines:
                report = []
                split_line = line.split()
                for element in split_line:
                    report.append(int(element))
                
                self.reports.append(report)

    # Idea: Iterate through each report. First, get the "direction" from the first and second
    # element. Check the direction of all elements after while also checking the difference.
    # O(mn) runtime where m = number of reports and n = size of longest report and O(1) size
    def solve_part_one(self):
        safe_reports = 0

        for report in self.reports:
            if self.check_report_safety(report):
                safe_reports += 1
        
        return safe_reports

    def check_report_safety(self, report: List[int]) -> bool:
        difference = self.calculate_difference_between_levels(report, 0)
        distance = abs(difference)
        if distance < 1 or distance > 3:
            return False

        monotonically_increasing = True if difference > 0 else False

        # Iterate starting from index 1 up to n - 1
        for i in range(1, len(report) - 1):
            iter_difference = self.calculate_difference_between_levels(report, i)
            iter_distance = abs(iter_difference)
            if iter_distance < 1 or iter_distance > 3:
                return False

            if monotonically_increasing and iter_difference < 0:
                return False
            elif not monotonically_increasing and iter_difference > 0:
                return False
        
        return True

    def calculate_difference_between_levels(self, report: List[int], curr_index: int) -> int:
        curr_level = report[curr_index]
        next_level = report[curr_index + 1]
        return next_level - curr_level
    
def main():
    solution = Solution(sys.argv[-1])
    part_one_value = solution.solve_part_one()
    print(f'Solution Part 1: {part_one_value}')

if __name__ == '__main__':
    main()