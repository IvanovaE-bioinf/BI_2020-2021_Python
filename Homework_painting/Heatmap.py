# Dataset Boston from MASS package (R), Housing values in suburbs of Boston
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.rcParams['savefig.bbox'] = 'tight'
data = pd.read_csv('boston.csv')
data.drop(data.columns[[0]], axis=1, inplace=True)
correlation_matrix = data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, ax=ax, cmap='YlGnBu', linewidth=0.1)
plt.suptitle('Correlation matrix')
plt.savefig('Boston_dataset_correlation_heatmap.png')
plt.show()








