python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load building completions data
building_data = pd.read_excel('Building_Completions_Abu_Dhabi.xlsx')

# Load public transport usage data
transport_data = pd.read_csv('Public_Transport_Usage_Abu_Dhabi.csv')

# Load healthcare facilities data
healthcare_data = gpd.read_file('Healthcare_Facilities_Abu_Dhabi.geojson')

# Merge datasets based on common fields, such as area or region
merged_data = building_data.merge(transport_data, on='Area')

# Analysis example: Correlation between building completions and public transport usage
correlation_matrix = merged_data.corr()
print(correlation_matrix['Public_Transport_Usage'])

# Visualization example: Plotting building completions and transport usage
fig, ax = plt.subplots()
merged_data.plot(kind='bar', x='Year', y=['Building_Completions', 'Public_Transport_Usage'], ax=ax)
plt.title('Building Completions vs Public Transport Usage in Abu Dhabi')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Save merged data for further analysis
merged_data.to_csv('Merged_Transport_Building_Data.csv', index=False)
