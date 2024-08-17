import pandas as pd
df = pd.read_csv('m3/u3/GooglePlayStore_wild.csv')
print(df.info())
df['Rating'].fillna(3, inplace = True)
print(df.info())
df.dropna(inplace= True)
print(df.info())
# Очищення даних із першого завдання

# Заміни тип даних на дробове число (float) для цін додатків (Price)
def rkfrmkom(Price):
    if Price[0] == '$':
        return float(Price[1:])
    else:
        return 0 
df['Price']=df ['Price'].apply(rkfrmkom)
print(df.info())
    
# Обчисли, скільки доларів розробники заробили на кожному платному додатку

# Чому дорівнює максимальний дохід ('Profit') серед платних додатків (Type == 'Paid')?
def mmo(he):
    return he.split(';')
df['Genres'] = df['Genres'].apply(mmo)
df['len Ghrec'] = df['Genres'].apply(len)
print(df.info())
print(df['len Ghrec'])
# Створи новий стовпець, у якому зберігатиметься кількість жанрів. Назви його 'Number of genres'

# Яка максимальна кількість жанрів (Number of genres) зберігається в датасеті?

# Бонусне завдання
# Створи новий стовпець, що зберігає сезон, в якому було зроблено останнє оновлення (Last Updated) програми. Назви його 'Season'

# Виведи на екран сезони та їх кількість у датасеті
