import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

names = ['TPSA', 'SAacc', 'H050', 'MLOGP', 'RDCHI', 'GATS1p', 'nN', 'C040', 'LC50']

df = pd.read_csv("qsar_aquatic_toxicity.csv", sep=";")
df.columns = names

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

count_vars = ['H050', 'nN', 'C040']

count_var = count_vars[0]

X_new = X.copy()

for count_var in count_vars:
    X_new.loc[X_new[count_var] > 0] = 1

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)




#X_train[count_var].loc[X_train[count_var] > 0] = 1

# for count_var in count_vars:
#     X_train.loc[X_train[count_var] > 0] = 1
#     X_test.loc[X_test[count_var] > 0] = 1
