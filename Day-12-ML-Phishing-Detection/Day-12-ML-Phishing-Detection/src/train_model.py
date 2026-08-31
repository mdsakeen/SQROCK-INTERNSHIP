import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

df=pd.read_csv('data/data.csv')
X_train,X_test,y_train,y_test=train_test_split(df.text,df.label,test_size=.3,random_state=42,stratify=df.label)
pipe=Pipeline([('vec',CountVectorizer()),('clf',MultinomialNB())])
pipe.fit(X_train,y_train); pred=pipe.predict(X_test)
acc=accuracy_score(y_test,pred); cm=confusion_matrix(y_test,pred)
print('Accuracy:',round(acc,4)); print('Confusion matrix:\n',cm); print(classification_report(y_test,pred))
open('output/metrics.txt','w').write(f'Accuracy: {acc:.4f}\nConfusion matrix:\n{cm}\n')
