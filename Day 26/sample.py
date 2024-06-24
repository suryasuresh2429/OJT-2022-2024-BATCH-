import pandas as pd

#Display the first few rows of the dataset.
data=pd.read_csv('sample_dataset.csv')
data.head()

#Generate summary statistics for this dataset. What are the mean and standard deviation of the Sepal Length?
print(data.describe())

#Check for any missing values in the dataset. How would you handle them if there were any?
data.isnull().sum()

#Convert the species labels to numerical values using a mapping dictionary. For example, map 'FlowerA' to 0, 'FlowerB' to 1, and 'FlowerC' to 2.
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC':2}
data['Species'] = data['Species'].map(species_mapping)
