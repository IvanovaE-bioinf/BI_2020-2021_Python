import pandas as pd
import matplotlib.pyplot as plt


# Plotting of the stacked barplot
plt.rcParams['savefig.bbox'] = 'tight'
train = pd.read_csv('train.csv')
pos = train['pos'].to_list()
nucleotides = train.filter(items=['A', 'T', 'G', 'C'])
nucleotides.index = pos
ax = nucleotides.plot(kind='bar', stacked=True, figsize=(10, 6))
ax.set_ylabel('$Frequencies$')
ax.set_xlabel('$Positions$')
plt.legend(title='labels', bbox_to_anchor=(1.0, 1), loc='upper left')
plt.savefig('stacked.png')
plt.show()

# Creating train_part.csv
matches_mean = train.loc[:, 'matches'].mean()
train_matches = train.query('matches > @matches_mean')
train_part = train_matches.filter(items=['pos',
                                         'reads_all',
                                         'mismatches',
                                         'deletions',
                                         'insertions'])
train_part.to_csv("train_part.csv", index=False)

