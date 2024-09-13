# Function to simulate the given program logic with specific values of A and B
def test_program(A, B):
    # Calculate intermediate value of A using the formula A = (A + B) * B
    A = (A + B) * B
    # Calculate the final output C by subtracting 5 from A
    C = A - 5
    return C

# Function to find and test all possible values of A for a given B
def find_values_for_B(B):
    results = []  # List to store results of each test case
    # Loop through a range of possible values for A (from -10 to 10)
    for A in range(-10, 11):
        # Calculate the result C for each value of A and B
        C = test_program(A, B)
        # Store the result as a tuple (A, C) in the results list
        results.append((A, C))
    return results

def main():
    B = 2  # Set the value of B to 2 as specified in Task 4
    # Find results by testing all values of A with B=2
    results = find_values_for_B(B)
    # Print the results in a readable format
    for A, C in results:
        print(f"A = {A}, C = {C}")

# Entry point of the program
if __name__ == "__main__":
    main()
