import pandas as pd

a = pd.read_csv('/home/andre/Documents/nova_dica.csv')
b = pd.read_csv('/home/andre/Documents/nova_dica_2.csv')
c = pd.concat([a,b], axis=0)

c.drop_duplicates(keep=False)
print(c)