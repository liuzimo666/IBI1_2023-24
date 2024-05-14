# Import the required Python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the full path to the data file
data_file_path = "C:\\Users\\13180\\Downloads\\dalys-rate-from-all-causes(1).csv%3FglobalNavigation=false (1).csv"

# Extract the directory path from the file path
data_directory_path = os.path.dirname(data_file_path)

# Change the working directory to the directory where the data file is located
os.chdir(data_directory_path)

# Confirm the current working directory
print("current working dictionary:", os.getcwd())

# Read the CSV file into the DataFrame object
dalys_data = pd.read_csv(os.path.basename(data_file_path))

# Show the fourth column (DALYs) starting from row 1, with data in 10 rows, up to row 100 (including row 100)
dalys_every_10th_row = dalys_data.iloc[0:100:10, 3] 
print("DALYs from every 10th row for the first 100 rows:")
print(dalys_every_10th_row)

# Display DALYs data for all Afghanistan using a Boolean index
afghanistan_dalys = dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'DALYs']
print("Afghanistan DALYs:")
print(afghanistan_dalys)

# Filter out the Chinese data and create a new DataFrame
china_data = dalys_data.loc[dalys_data['Entity'] == 'China', ['Year', 'DALYs']]

# Calculate the average DALYs in China using numpy
mean_dalys_china = np.mean(china_data['DALYs'])
print(f"Mean DALYs in China: {mean_dalys_china}")

# Find the DALYs in China in 2019 and compare them with the average
china_2019_dalys = china_data.loc[china_data['Year'] == 2019, 'DALYs'].values[0]
if china_2019_dalys > mean_dalys_china:
    comparison = "greater"
else:
    comparison = "less"
print(f"DALYs in China in 2019 was {comparison} than the mean.")

# Plot the DALYs of China over time
plt.figure(figsize=(10, 5))
plt.plot(china_data['Year'], china_data['DALYs'], 'b+') 
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Time in China')
# Rotate the X-axis labels so that they are easier to read
plt.xticks(rotation=-90)
plt.tight_layout()  
plt.show()






#question
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = "C:\\Users\\13180\\Downloads\\dalys-rate-from-all-causes(1).csv%3FglobalNavigation=false (1).csv"
dalys_data = pd.read_csv(file_path)

# Sift out data for China and the UK
china_data = dalys_data[dalys_data['Entity'] == 'China']
uk_data = dalys_data[dalys_data['Code'] == 'GBR']

# The average DALYs for China and the UK were calculated
mean_dalys_china = china_data['DALYs'].mean()
mean_dalys_uk = uk_data['DALYs'].mean()

# Create a chart comparing DALYs in China and the UK over time
plt.figure(figsize=(14, 7))
plt.plot(china_data['Year'], china_data['DALYs'], label='China', marker='o')
plt.plot(uk_data['Year'], uk_data['DALYs'], label='UK', marker='x')

# Add the title and legend of the chart
plt.title('Comparison of DALYs Over Time in China and the UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()