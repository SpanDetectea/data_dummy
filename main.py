import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'whoAmI_Dummy'] = 0
data.loc[data['whoAmI'] == 'human', 'whoAmI_Dummy'] = 1
dum = pd.get_dummies(data, columns=['whoAmI'])
dum