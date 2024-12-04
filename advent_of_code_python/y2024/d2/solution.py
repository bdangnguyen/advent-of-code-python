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
    # Time: O(mn) where m = number of reports and n = size of longest report
    # Space: O(1) 
    def solve_part_one(self):
        safe_reports = 0

        for report in self.reports:
            if self.check_report_safety(report):
                safe_reports += 1
        
        return safe_reports
    
    # Idea: Brute force this and check all possible sub list combinations.
    # Edge case 1: Removal of problem level causes a new issue I.e. 1 9 10, 6 2 1.
    # Edge case 2: Removal of second level, then we need to also consider the new direction. To 
    # solve this, we should remove the next element from the list and continue in place. 
    # Edge case 3: First element is possible to be removed to be safe. In this situation, need to
    # evaluate the entire remaining sublist for safety.
    # Time: O(mn^2) where m = number of reports and n = length of longest levels
    # Space: O(n)
    def solve_part_two(self):
        safe_reports = 0

        for report in self.reports:
            if self.check_report_safety_with_problem_dampener(report):
                safe_reports += 1

        return safe_reports
    
    def check_report_safety_with_problem_dampener(self, report: List[int]) -> bool:
        for i in range(0, len(report)):
            dampened_list = report.copy()
            dampened_list.pop(i)
            if self.check_report_safety(dampened_list):
                return True
            
        return False
    
    def check_report_safety(self, report: List[int]) -> bool:
        monotonically_increasing = True

        for i in range(0, len(report) - 1):
            difference = report[i + 1] - report[i]
            if i == 0:
                monotonically_increasing = True if difference > 0 else False 
            distance = abs(difference)
            
            if distance < 1 or distance > 3:
                return False
            if ((monotonically_increasing and difference < 0) 
                or (not monotonically_increasing and difference > 0)):
                return False
        
        return True
    
def main():
    solution = Solution(sys.argv[1])
    part_one_value = solution.solve_part_one()
    part_two_value = solution.solve_part_two()
    print(f'Solution Part 1: {part_one_value}')
    print(f'Solution Part 2: {part_two_value}')

if __name__ == '__main__':
    main()