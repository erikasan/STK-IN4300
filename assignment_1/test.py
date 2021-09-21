import pandas as pd

index = pd.read_table('adult.names', skiprows=97)

df = pd.read_table('adult.data')
#df.set_index(index)
