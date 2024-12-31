import pandas as pd
df = pd.read_csv('ClimateChangeData.csv')
# part 1
#How many records are included in the dataframe?
count = df.shape[0]
print(count)
# Are there any missing values in the given dataset? If so, how many?
missing_values = df.isnull().sum().sum()
print (missing_values)
#How do you plan on handling the missing values in the given dataset? Justify your answer
data = pd.read_csv('ClimateChangeData.csv')
missing_data1 = data.select_dtypes(include=['float64']).columns
data[missing_data1] = (data[missing_data1].ffill() + data[missing_data1].bfill()) / 2
missing_data2 = data.select_dtypes(include=['object']).columns
data[missing_data2] = data[missing_data2].fillna('Unknown')
print(data)
#) How many countries have missing values? Create a list of countries that contains missingvalues.
countries_missing_values = data['Country'].unique()
num_countries_missing_values = len(countries_missing_values)
print(countries_missing_values)
#Create a new dataframe after handling the missing values as you have decided in
new_data = data.copy()
new_data_path = ('ClimateChangeData.csv')
new_data.to_csv(new_data_path, index=False)


#part 2
new_data_path = pd.read_csv('ClimateChangeData.csv')

# How many different countries are listed in this dataframe?
count = new_data_path['Country'].nunique()
print(count)

# Create a new column, “Mean Temp. Change”, in the dataframe containingthemeantemperature change for each country.
temperature_columns_valid = [col for col in new_data_path.columns if col.startswith('Temp')]
new_data_path['Mean Temp. Change'] = new_data_path[temperature_columns_valid].mean(axis=1)
print(new_data_path[['Country', 'Mean Temp. Change']].head())

# Create a new dataframe with two columns. One containing the years (1967-2023), andtheother containing the mean temperature change for 
df = pd.read_csv('ClimateChangeData.csv')
years = [str(year) for year in range(1967, 2024)]
yearly_data = df[years]
transposed_data = yearly_data.transpose()
transposed_data['Mean Temperature Change'] = transposed_data.mean(axis=1)
mean_temp_df = transposed_data[['Mean Temperature Change']]
print(mean_temp_df)
