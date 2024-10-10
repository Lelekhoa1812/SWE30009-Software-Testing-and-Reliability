# Name: Dang Khoa Le 
# Student ID: 103844421

import copy

# Import matrix_multiplication_recursion from the SUT folder
# This is the original program where we use its matrix_multiply_recursive algorithm
from ..SUT.matrix_multiplication_recursion import matrix_multiply_recursive
# Import mutants from the MUTANTS folder
from ..MUTANTS.mutation1 import matrix_multiply_recursive as m1
from ..MUTANTS.mutation2 import matrix_multiply_recursive as m2
from ..MUTANTS.mutation3 import matrix_multiply_recursive as m3
from ..MUTANTS.mutation4 import matrix_multiply_recursive as m4
from ..MUTANTS.mutation5 import matrix_multiply_recursive as m5
from ..MUTANTS.mutation6 import matrix_multiply_recursive as m6
from ..MUTANTS.mutation7 import matrix_multiply_recursive as m7
from ..MUTANTS.mutation8 import matrix_multiply_recursive as m8
from ..MUTANTS.mutation9 import matrix_multiply_recursive as m9
from ..MUTANTS.mutation10 import matrix_multiply_recursive as m10
from ..MUTANTS.mutation11 import matrix_multiply_recursive as m11
from ..MUTANTS.mutation12 import matrix_multiply_recursive as m12
from ..MUTANTS.mutation13 import matrix_multiply_recursive as m13
from ..MUTANTS.mutation14 import matrix_multiply_recursive as m14
from ..MUTANTS.mutation15 import matrix_multiply_recursive as m15
from ..MUTANTS.mutation16 import matrix_multiply_recursive as m16
from ..MUTANTS.mutation17 import matrix_multiply_recursive as m17
from ..MUTANTS.mutation18 import matrix_multiply_recursive as m18
from ..MUTANTS.mutation19 import matrix_multiply_recursive as m19
from ..MUTANTS.mutation20 import matrix_multiply_recursive as m20
from ..MUTANTS.mutation21 import matrix_multiply_recursive as m21
from ..MUTANTS.mutation22 import matrix_multiply_recursive as m22
from ..MUTANTS.mutation23 import matrix_multiply_recursive as m23
from ..MUTANTS.mutation24 import matrix_multiply_recursive as m24
from ..MUTANTS.mutation25 import matrix_multiply_recursive as m25
from ..MUTANTS.mutation26 import matrix_multiply_recursive as m26
from ..MUTANTS.mutation27 import matrix_multiply_recursive as m27
from ..MUTANTS.mutation28 import matrix_multiply_recursive as m28
from ..MUTANTS.mutation29 import matrix_multiply_recursive as m29
from ..MUTANTS.mutation30 import matrix_multiply_recursive as m30

# Usage: python mutant_testing.py or python3 mutant_testing.py

# 5 Test Groups (Matrix A, B)
test_cases = [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]]), # Test group 1
    ([[9, 8], [7, 6]], [[5, 4], [3, 2]]), # Test group 2
    ([[0, 0], [1, 1]], [[3, 3], [4, 4]]), # Test group 3
    ([[0, 9], [1, 8]], [[2, 7], [3, 6]]), # Test group 4
    ([[1, 1], [1, 1]], [[7, 7], [7, 7]])  # Test group 5
]

# Mutants list and labelling (for output demonstration as a string)
mutants = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25, m26, m27, m28, m29, m30]  
mutant_labels = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20', 'm21', 'm22', 'm23', 'm24', 'm25', 'm26', 'm27', 'm28', 'm29', 'm30']

# Initialise variables for MS calculation
total_mutants = len(mutants)
total_test_groups = len(test_cases)
results = {label: {'MR1': False, 'MR2': False, 'Overall': False} for label in mutant_labels} # Tracks result

# MR1: Scaling the matrix (multiply all values by 2)
def mr1():
    test_group_index = 1 # Initialize the test group counter
    killed_per_group_mr1 = []  # Track the number of killed mutants per group in MR1
    for matrix_a, matrix_b in test_cases:  # Loop through each test case (matrix A and B pairs)
        # Multiply each element in matrix_a and matrix_b by 2 (scaling the matrix)
        scaled_a = [[x * 2 for x in row] for row in matrix_a]
        scaled_b = [[x * 2 for x in row] for row in matrix_b]
        test_results = []  # Track test results for each mutant in this group
        # Recursion checking, loop through each mutant and its label
        for mutant, label in zip(mutants, mutant_labels):
            result = mutant(scaled_a, scaled_b)                             # Get result of the mutant program
            expected_result = matrix_multiply_recursive(scaled_a, scaled_b) # Get result of the original program
            if result == expected_result: # Compare results
                test_results.append(f'Test Group {test_group_index} MR1 {label} passed')                                              # Print passed mutant
            else:
                test_results.append(f'Test Group {test_group_index} MR1 {label} failed (Expected: {expected_result}, Got: {result})') # Print killed mutant
                results[label]['MR1'] = True     # Mark this mutant as killed by MR1
                results[label]['Overall'] = True # Mark this mutant as killed by overall
        print("\n".join(test_results))  # Print test results for the group
        killed_count = count_killed_mutants(test_results)
        killed_per_group_mr1.append(killed_count)  # Track how many mutants were killed in this group
        test_group_index += 1 # Cycle to next test group
        print("--------------------------------------------------------------") # Breaker after complete 1 test group
    return killed_per_group_mr1  # Return list of killed mutants per each test groups by MR1

# MR2: Replace the last row of matrix_a and the last column of matrix_b with zeros
def mr2():
    test_group_index = 1 # Initialize the test group counter
    killed_per_group_mr2 = []  # Track the number of killed mutants per group in MR2
    for matrix_a, matrix_b in test_cases:  # Loop through each test case (matrix A and B pairs)
        matrix_a_extended = copy.deepcopy(matrix_a) # Use deepcopy when copy matrix value,
        matrix_b_extended = copy.deepcopy(matrix_b) # to avoid modifying the original test cases
        # Replace the last row of matrix_a with zeros
        matrix_a_extended[-1] = [0] * len(matrix_a[-1])
        # Replace the last column of matrix_b with zeros
        for row in matrix_b_extended:
            row[-1] = 0
        test_results = []  # Track test results for each mutant in this group
        # Recursion checking, loop through each mutant and its label
        for mutant, label in zip(mutants, mutant_labels): 
            result = mutant(matrix_a_extended, matrix_b_extended)                             # Get result of the mutant program
            expected_result = matrix_multiply_recursive(matrix_a_extended, matrix_b_extended) # Get result of the original program
            if result == expected_result: # Compare results
                test_results.append(f'Test Group {test_group_index} MR2 {label} passed')                                              # Print passed mutant
            else:
                test_results.append(f'Test Group {test_group_index} MR2 {label} failed (Expected: {expected_result}, Got: {result})') # Print killed mutant
                results[label]['MR2'] = True     # Mark this mutant as killed by MR1
                results[label]['Overall'] = True # Mark this mutant as killed by overall
        print("\n".join(test_results))  # Print test results for the group
        killed_count = count_killed_mutants(test_results)
        killed_per_group_mr2.append(killed_count)  # Track how many mutants were killed in this group
        test_group_index += 1 # Cycle to next test group
        print("--------------------------------------------------------------") # Breaker after complete 1 test group
    return killed_per_group_mr2  # Return list of killed mutants per each test groups by MR2

# Mutation Score Calculation
def calculate_mutation_score(killed_mr1, killed_mr2):
    print("\nMutant Score (MS) results:")
    print("Mutant   Detected by MR1   Detected by MR2   Detected Overall")

    # Track total number of killed mutant for MR1, MR2 and overall (either or both MR1 and MR2)
    total_killed_mr1 = sum(killed_mr1)
    total_killed_mr2 = sum(killed_mr2)
    total_mutants_killed = sum(1 for label in mutant_labels if results[label]['Overall'])

    # Display mutant detection details
    for label in mutant_labels:
        mr1_detected = "Yes" if results[label]['MR1'] else "No"
        mr2_detected = "Yes" if results[label]['MR2'] else "No"
        overall_detected = "Yes" if results[label]['Overall'] else "No"
        print(f"{label:<8} {mr1_detected:<17} {mr2_detected:<17} {overall_detected:<17}") # Print table with data and margin in between

    # Calculate average mutation scores per each MR (MSaverage = (k1+k2+...+kn) / (m*n))
    ms_mr1 = total_killed_mr1 / (total_mutants * total_test_groups)
    ms_mr2 = total_killed_mr2 / (total_mutants * total_test_groups)
    # Mutation score for test suite combining all test groups (MStest_suite = (𝐀1+𝐀2+...+𝐀m) / m)
    ms_test_suite = total_mutants_killed / total_mutants

    # Print mutation score results
    print(f"\nTotal mutants tested: {total_mutants}")
    print(f"Total mutants killed: {total_mutants_killed}\n")
    print(f"MR1 MSaverage: {ms_mr1:.2f}")
    print(f"MR2 MSaverage: {ms_mr2:.2f}")
    print(f"\nMStest_suite: {ms_test_suite:.2f}")

# Helper to count killed mutants in each MR
def count_killed_mutants(test_results):
    killed_count = 0
    for mutant_result in test_results:
        if 'failed' in mutant_result:  # Check if the mutant was killed (e.g., containing 'failed' notation)
            killed_count += 1
    return killed_count

# Run the tests
killed_mr1 = mr1()
print("##############################################################") # Breaker after complete 1 MR
print("--------------------------------------------------------------") # Sub-Breaker after complete 1 MR
killed_mr2 = mr2()
print("##############################################################") # Breaker after complete 1 MR
print("--------------------------------------------------------------") # Sub-Breaker after complete 1 MR
calculate_mutation_score(killed_mr1, killed_mr2)
