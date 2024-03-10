# Comment:
# Define a variable n to keep track of the current member of the sequence.
# Define a variable sequence to store the generated sequence.
# Define a variable previous1 and previous2 to store the two preceding members of the sequence.
# Set previous1 to the first member of the sequence, which is 4.
# Set previous2 to the second member of the sequence, which is 11.
# Start a loop that will iterate 5 times to generate the first five values of the sequence.
# Inside the loop, calculate the current member of the sequence using the equation current = 2 * previous1 + 3.


# Initialize Variables
n = 0  # Counter for the current member of the sequence
sequence = []  # List to store the generated sequence
previous1 = 4  # First member of the sequence
previous2 = 11  # Second member of the sequence

# Generate the Sequence
while n < 5:
    # Calculate the current member using the equation
    current = 2 * previous1 + 3

    sequence.append(previous1)
    
    # Update previous1 and previous2 for the next iteration
    previous2 = previous1
    previous1 = current
    
    # Increment the counter
    n += 1

# Display the Sequence
print("The first five values of the sequence are:", sequence)