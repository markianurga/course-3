import pandas as pd
df = pd.read_csv('m3/u2/GoogleApps.csv')
teen = df['Content Rating'].value_counts()
red = teen['Everyone 10+']
print (red)
con = teen['Everyone']
print(con)
print (con / red)
print(df.groupby(by = 'Content Rating')['Size'].mean())
op = (df.groupby(by = ['Type','Content Rating'])['Size'].agg(['min','max']))
#print (op ['max']['Teen']['Paid'])
print (op.reset_index())
ip = df.pivot_table(
    columns= 'Type',
    index=  'Content Rating',
    values=  'Size',
    aggfunc= 'min'
)
print (ip)