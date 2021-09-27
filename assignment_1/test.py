import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

features = []
output = ''

with open('adult.names') as infile:
    info = infile.readlines()
    output = info[94]
    for line in info[96:]:
        words = line.split()
        features.append(words[0])


for i in range(len(features)):
    features[i] = features[i][:-1]

# print("Feature names:\n", features, '\n')
# print("Output name:\n", output)

df = pd.read_csv('adult.data')
df.columns = features + [output]


def get_info(feature):
    column = df[[feature]].sort_values(by=feature)
    mean   = column.mean()
    std    = column.std()
    median = column.median()
    q3, q1 = np.percentile(column, [75 ,25])
    max    = column.max()
    min    = column.min()
    print('mean: ',   mean)
    print('std: ',    std)
    print('median: ', median)
    print('q1: ',     q1)
    print('q3: ',     q3)
    print('min: ',    min)
    print('max: ',    max)

def p(n):
    return n*100/32560

sns.set()
#sns.scatterplot(data=df, x='education', y='hours-per-week', hue='native-country')
#sns.scatterplot(data=df, x='native-country', y='hours-per-week', hue='education-num')
# sns.scatterplot(data=df, x='age', y='hours-per-week', hue='sex')
# plt.show()

# sns.lineplot(data=df, x='age', y='hours-per-week', hue='sex')
# plt.show()

sns.histplot(data=df, x='age', y='hours-per-week', hue='sex')
plt.show()
