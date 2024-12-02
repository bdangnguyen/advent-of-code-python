import advent_of_code_python.y2024.d1.solution as d1

def test_day_1_sample():
    solution = d1.Solution('sample.txt')
    
    assert solution.solve_part_one() == 11

def test_day_2_sample():
    solution = d1.Solution('sample.txt')
    
    assert solution.solve_part_two() == 31