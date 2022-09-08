from sklearn import preprocessing
import pandas as pd

df = pd.read_csv('FullDataset2022-07-28.csv')

le = preprocessing.LabelEncoder()
#each column may need its own label encoder?
#consider looping through df and making an encoder for each one and storing in a dict