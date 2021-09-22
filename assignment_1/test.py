import numpy as np
import pandas as pd

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

print("Feature names:\n", features, '\n')
print("Output name:\n", output)

df = pd.read_csv('adult.data')
df.columns = features + [output]

df[['age']].mean()

def get_info(feature):
    mean = df[[feature]].mean()
    std = df[[feature]].std()
    median = df[[feature]].median()
    q3, q1 = np.percentile(df[[feature]], [75 ,25])
    max = df[[feature]].max()
    min = df[[feature]].min()
    print('mean: ', mean)
    print('std: ', std)
    print('median: ', median)
    print('q1: ', q1)
    print('q3: ', q3)
    print('min: ', min)
    print('max: ', max)

def p(n):
    return n*100/32560
