### 2
import pandas as pd

# Load the CSV
df = pd.read_csv('task\\stackoverflow_qa.csv', parse_dates=['creationdate'])

# 1
df[df['creationdate'] < '2014-01-01']
# 2
df[df['score'] > 50]
# 3
df[(df['score'] >= 50) & (df['score'] <= 100)]
# 4
df[df['quest_name'] == 'Scott Boston']
# 5
users = ['Scott Boston', 'tatwright', 'David Underhill', 'yueerhu', 'DarkAnt']
df[df['quest_name'].isin(users)]

# 6
mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['quest_name'] == 'Unutbu') &
    (df['score'] < 5)
)
df[mask]
# 7
df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
# 8
df[df['quest_name'] != 'Scott Boston']


### 3
import pandas as pd

# Load the dataset
titanic_df = pd.read_csv("task\\titanic.csv")

# 1
females_class1_age_20_38 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 38))
]
# 2
paid_over_100 = titanic_df[titanic_df['Fare'] > 100]
# 3
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
# 4
embarked_c_paid_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
# 5
with_family = titanic_df[
    (titanic_df['SibSp'] > 0) | (titanic_df['Parch'] > 0)
]
# 6
high_fare_with_cabin = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]
# 7
not_survived = titanic_df[titanic_df['Survived'] == 0]
# 8
miss_females_class1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Name'].str.contains("Miss", case=False, na=False))
]
