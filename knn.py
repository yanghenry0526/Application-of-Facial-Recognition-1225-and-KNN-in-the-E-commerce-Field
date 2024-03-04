import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

read_file = pd.read_excel(r'./ComDataSave.xlsx')
read_file.to_csv('ComDataSave.csv', index=None, header=True,encoding='UTF-8-Sig')
df = pd.read_csv('ComDataSave.csv')

# 取得訓練的資料，x是變量，ｙ是種類
x = df[['性別', '年齡', '表情', 'time(s)']].values
y = df['tempTcode'].values

#Train Model and Predict
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
k = 7
knn = KNeighborsClassifier().fit(X_train, y_train)
joblib.dump(knn, 'knn.model')

