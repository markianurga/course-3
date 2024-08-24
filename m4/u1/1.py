import pandas as pd
df = pd.read_csv('m4/u1/titanic.csv')
print(df.info())
df.drop('Name', axis = 1,
        inplace = True)
df.drop('Ticket', axis = 1,
        inplace = True)
df.drop('Cabin', axis = 1,
        inplace = True)
df.drop('PassengerId', axis = 1,
        inplace = True)
print(df.info())

df['Embarked'].fillna('S', inplace = True)
df['Age'].fillna(df['Age'].mean(), inplace = True)
print(df.info())

def rkfrmkom(Sex):
    if Sex == 'male':
        return 1
    else:
        return 0 
df['Sex']=df ['Sex'].apply(rkfrmkom)
print(df.info())