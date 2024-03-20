# Create a dictionary with the activity data
activity_data = {
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1
}
# Calculate the remaining hours in the day and add them to the 'other' category
total_hours_in_day = 24
remaining_hours = total_hours_in_day - sum(activity_data.values())
activity_data['Other'] = remaining_hours
# Print the dictionary
print("Activity Data Dictionary:")
for activity, hours in activity_data.items():
    print(f"{activity}: {hours} hours")


import matplotlib.pyplot as plt
# Create a pie chart
labels = activity_data.keys()
sizes = activity_data.values()
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Average Day of a University Student')
plt.axis('equal')  # Ensure that the pie chart is drawn as a circle
plt.show()


# suppose we want to check the average time of the "sleeping"
activity_to_query = 'Sleeping'
hours_spent = activity_data[activity_to_query]
print(f"The average number of hours spent on {activity_to_query} during an average day is {hours_spent} hours.")
