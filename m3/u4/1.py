import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('m3/u4/GoogleApps.csv')
#df['Size'].plot(kind = 'hist')
#plt.show()
#df[df['Type'] == 'Paid']['Price'].plot(kind = 'box')
#plt.show()
#df['Category'].value_counts().plot(kind = 'pie')
#plt.show()
df.plot(x = 'Rating', y = 'Installs', kind = 'scatter')
plt.show()
