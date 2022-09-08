from random import random
import pandas as pd
from sklearn.datasets import load_iris

from sklearn.preprocessing import LabelEncoder
from sklearn import tree
df = pd.read_csv('FullDataset2022-07-28.csv')

df = df.dropna(subset=['SuicideConsidered_M'])

inputs = df.loc[:, ('TimeToBed','ElapsedWokeUp','NumWokeUp')]
target = df['SuicideConsidered_M']

le_timetobed = LabelEncoder()
le_elapsedwokeup = LabelEncoder()
le_numwokeup = LabelEncoder()

inputs['TimeToBed_n'] = le_timetobed.fit_transform(inputs['TimeToBed'])
inputs['ElapsedWokeUp_n'] = le_elapsedwokeup.fit_transform(inputs['ElapsedWokeUp'])
inputs['NumWokeUp_n'] = le_numwokeup.fit_transform(inputs['NumWokeUp'])

inputs_n = inputs.drop(['TimeToBed','ElapsedWokeUp','NumWokeUp'], axis='columns')

model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)

clf = tree.DecisionTreeClassifier(random_state=0)
iris = load_iris()

clf.fit(iris.data, iris.target)
tree.plot_tree(clf)

print('Model Score: ' + str(model.score(inputs_n,target)))
print(inputs)
print(model.predict([[0,20,4]]))
#tree.plot_tree(model)