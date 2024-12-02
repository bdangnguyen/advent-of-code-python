import advent_of_code_python.y2024.d2.solution as d2

def test_day_1_sample():
    solution = d2.Solution('sample.txt')
    
    assert solution.solve_part_one() == 2

def test_day_2_sample():
    solution = d2.Solution('sample.txt')
    
    assert solution.solve_part_two() == 31