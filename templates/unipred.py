

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset =  pd.read_csv('puphy.csv')

import pickle
dataset['Year of passing '] = dataset['Year of passing '].fillna(2018)
dataset['Deduction '] = dataset['Deduction'].fillna(0)

x= dataset.iloc[:,:-1]

y = dataset.iloc[:,-1]

np.isnan(dataset)
np.where(np.isnan(dataset))
np.nan_to_num(x)



from sklearn.model_selection  import train_test_split

x_train,x_test, y_train,y_test = train_test_split(x,y,test_size =0.2)


from sklearn.linear_model import LogisticRegression

regression  = LogisticRegression()

regression.fit(x_train,y_train)



y_pred = regression.predict(x_train)


score = regression.score(x_train,y_train)
print(score*100)


pickle.dump(regression, open('model2.pkl','wb'))

# Loading model to compare the results0.

model = pickle.load(open('model2.pkl','rb'))

print(model.predict([[1,10,2018,0,35,20,0,55]]))