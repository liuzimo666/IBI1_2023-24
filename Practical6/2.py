import matplotlib.pyplot as plt

# define urban population for UK and China
uk_cities = {'Edinburgh': 0.56, 'Glasgow': 0.62, 'Stirling': 0.04, 'London': 9.7}
china_cities = {'Haining': 0.58, 'Hangzhou': 8.4, 'Shanghai': 29.9, 'Beijing': 22.2}

# sort urban population for UK and China
sorted_uk_cities_population = sorted(uk_cities.items(), key=lambda x: x[1])
sorted_china_cities_population = sorted(china_cities.items(), key=lambda x: x[1])

print("Sorted UK cities by population:")
for city, population in sorted_uk_cities_population:
  print(f"{city}: {population:.2f} millions")

print("\nSorted China cities by population:")
for city, population in sorted_china_cities_population:
  print(f"{city}: {population:.2f} millions")

# chart the population bar of UK
plt.figure(figsize=(10, 5))
plt.bar([city for city, _ in sorted_uk_cities_population], [population for _, population in sorted_uk_cities_population], label='UK City Populations')
plt.xlabel('Cities')
plt.ylabel('Population (millions)')
plt.title('Distribution of City Sizes in the UK')
plt.xticks(rotation=45) 
plt.legend()
plt.show()
# chart the population bar for China
plt.figure(figsize=(10, 5))
plt.bar([city for city, _ in sorted_china_cities_population], [population for _, population in sorted_china_cities_population], label='China City Populations')
plt.xlabel('Cities')
plt.ylabel('Population (millions)')
plt.title('Distribution of City Sizes in China')
plt.xticks(rotation=45) 
plt.legend()
plt.show()
