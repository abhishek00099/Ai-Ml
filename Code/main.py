import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


file_path = "C:\Users\ABHISHEK\Downloads\TitanicDataset.csv"
df = pd.read_csv(file_path)


df_info = df.info()
df_head = df.head()
df_nulls = df.isnull().sum()

df_head, df_info, df_nulls


df['Age'].fillna(df['Age'].median(), inplace=True)  
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  
df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True)  


le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])  
df['Embarked'] = le.fit_transform(df['Embarked'])


scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])


for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]


df_cleaned_info = df.info()
df_cleaned_head = df.head()

df_cleaned_info, df_cleaned_head

output_path = "C:\Users\ABHISHEK\Downloads/Titanic_Cleaned.csv"
df.to_csv(output_path, index=False)