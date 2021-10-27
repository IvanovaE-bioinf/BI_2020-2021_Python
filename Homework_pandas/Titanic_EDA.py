import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


titanic = pd.read_csv('titanic.csv')
# Size - 891 observations and 12 variables
size = titanic.shape

# Types - some variables should be of categorical type
variable_types = titanic.dtypes

# NA - 3 variables have NA, mostly information about cabin
count_NA = titanic.isna().sum()

# Conversion to categories
titanic = titanic.astype({'Survived': 'category',
                          'Pclass': 'category',
                          'SibSp': 'category',
                          'Parch': 'category',
                          'Embarked': 'category',
                          'Sex': 'category'})
titanic_survived = titanic.query("Survived == 1")

# Distribution
plt.rcParams['figure.figsize'] = [16, 8]
fig, axes = plt.subplots(nrows=2, ncols=4, constrained_layout=True)
titanic_survived['Sex'].value_counts().plot.bar(ax=axes[0, 0],
                                                color='xkcd:aqua',
                                                rot=360, grid=True,
                                                title='Survived')
titanic['Sex'].value_counts().plot.bar(ax=axes[0, 1],
                                       color='xkcd:aqua',
                                       rot=360, grid=True,
                                       title='Gender')
titanic['Pclass'].value_counts().plot.bar(ax=axes[0, 2],
                                          color='xkcd:aqua',
                                          rot=360, grid=True,
                                          title='Passenger class')
titanic['SibSp'].value_counts().plot.bar(ax=axes[0, 3],
                                         color='xkcd:aqua',
                                         rot=360, grid=True,
                                         title='Passengers with sib. and parents')
titanic['Parch'].value_counts().plot.bar(ax=axes[1, 0],
                                         color='xkcd:aqua',
                                         rot=360, grid=True,
                                         title='Passengers with parents')
titanic['Embarked'].value_counts().plot.bar(ax=axes[1, 1],
                                            color='xkcd:aqua',
                                            rot=360, grid=True,
                                            title='Where embarked')
titanic['Age'].plot.\
    hist(ax=axes[1, 2], color='xkcd:wheat', grid=True, title='Age')
titanic['Fare'].plot.\
    hist(ax=axes[1, 3], color='xkcd:wheat', grid=True, title='Fare')
plt.suptitle('Distributions of the variables')
plt.savefig('Distribution.png')
plt.show()
# There were more men then women.
# More women survived then men.
# The most part of passengers was in the 3rd class.
# The most part of passengers embarked in Southampton (S).
# The middle age of passengers is about 30.
plt.close()

# Correlation
partial = titanic.filter(items=['Survived',
                                'Pclass',
                                'Sex',
                                'Age',
                                'SibSp',
                                'Parch',
                                'Fare'])
partial = partial.astype({'Survived': 'int',
                          'Pclass': 'int',
                          'SibSp': 'int',
                          'Parch': 'int'})
correlation_matrix = partial.corr()
_, ax = plt.subplots()
sns.heatmap(correlation_matrix,
            ax=ax, linewidth=0.1,
            cmap='Greens',
            annot=True)
plt.suptitle('Correlation matrix')
plt.savefig('Heatmap.png')
plt.show()
plt.close()
# A weak correlation between Pclass/Fare - obviously 3rd class is cheaper;
# between Pclass/Survived - passengers of the 3rd class mostly died;
# between Pclass/Age - older people have money for the 1st class;
# between Age/SibSp - the older the passenger the less relatives on board;
# between SibSp/Parch - parents+siblings==parents+children.
# Seems that gender and class were the most important factors for survival.
