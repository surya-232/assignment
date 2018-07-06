import pandas as p
import numpy as np

d = {
    'name' : ['surya','ashwani','charu','shivam','karna'],
    'age' : [19,20,20,21,21],
    'mail_id' : ['saxenasurya001@gmail.com','ashwani6969@gmail.com','charuvashist@gmail.com','sainikalaunda@gmail.com','abikarna@gmail.com'],
    'ph_number' : [9053408984,9053408998,9053408984,9053408984,9999999999]
}
df=p.DataFrame(d)
print(df)


df=p.read_csv('s.csv')
print(df)
print(df.head(5))
print(df[0:5])
print(df.head(10))
print(df.describe())
print(df.tail(5))
print(df['Location'].describe())