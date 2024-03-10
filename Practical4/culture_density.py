# Define the initial cell density as a percentage
initial_density = 5

# Define the maximum cell density before they start dying
max_density = 90

# Initialize the current day as 1
current_day = 1

# Initialize a loop that will continue until the cell density exceeds the maximum density
while initial_density <= max_density:
    # Print the current day and cell density
    print(f"Day {current_day}: Cell Density = {initial_density}%")
    
    # Increase the cell density by doubling it (as stated in the problem)
    initial_density *= 2
    
    # Increment the current day
    current_day += 1

print(f"Cell density exceeded 90% on Day {current_day - 1}.")
print(f"Therefore, you can take a holiday from the lab for {current_day - 2} days.")

