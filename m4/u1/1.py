from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('m4/u1/titanic.csv')
#print(df.info())
df.drop('Name', axis = 1,
        inplace = True)
df.drop('Ticket', axis = 1,
        inplace = True)
df.drop('Cabin', axis = 1,
        inplace = True)
df.drop('PassengerId', axis = 1,
        inplace = True)
#print(df.info())

df['Embarked'].fillna('S', inplace = True)
df['Age'].fillna(df['Age'].mean(), inplace = True)
#print(df.info())

def rkfrmkom(Sex):
    if Sex == 'male':
        return 1
    else:
        return 0 
df['Sex']=df ['Sex'].apply(rkfrmkom)
#print(df.info())

df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis = 1,
        inplace = True)
#print(df.info())
#print(df)


x = df.drop('Survived', axis = 1)
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#print(x_test, x_train)

ter = KNeighborsClassifier(n_neighbors = 500)
ter.fit(x_train, y_train)


ou = ter.predict(x_test)

ow = accuracy_score(y_test, ou) 
print('відцоток почності беребачиннь')
print(ow * 100)