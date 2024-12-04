import advent_of_code_python.y2024.d1.solution as d1
import advent_of_code_python.y2024.d2.solution as d2


def test_day_1_sample_1():
    solution = d1.Solution('sample.txt')
    
    assert solution.solve_part_one() == 11

def test_day_1_sample_2():
    solution = d1.Solution('sample.txt')
    
    assert solution.solve_part_two() == 31

def test_day_2_sample_1():
    solution = d2.Solution('sample.txt')
    
    assert solution.solve_part_one() == 2

def test_day_2_sample_2():
    solution = d2.Solution('sample.txt')
    
    assert solution.solve_part_two() == 4