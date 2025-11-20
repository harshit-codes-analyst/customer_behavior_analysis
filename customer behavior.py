import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("customer_shopping_behavior.csv")
head = df.head()
info = df.info()
des = df.describe(include="all")
null = df.isnull().sum() # check null values

df['Review Rating'] = df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median())) #fill null values
null = df.isnull().sum()

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
df = df.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})
print(df.columns)

#create a new column age_group
labels = ['Young Adult','Adult','Middle-aged','Senior']   # Create category names for age groups
df["age_group"] = pd.qcut(df["age"], q=4, labels=labels)  # Divide 'age' column into 4 equal frequency bins and assign labels
check = df[['age','age_group']].head(10)                  # Select first 10 rows showing only 'age' and 'age_group' columns
print(check)                                             # Print the result to view age and its respective group

## Create a dictionary that maps purchase frequency terms to the number of days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly' : 7,
    'Monthly': 30,
    'Quarterly' : 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months' : 90
}
# Map the 'frequency_of_purchases' column to corresponding days using the dictionary
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
# Select and view the last 10 rows of the two relevant columns to check mapping results
check1 = df[['purchase_frequency_days','frequency_of_purchases']].tail(10)
print(check1)

acc = df[['discount_applied','promo_code_used']].head(10)
acc1 = (df['discount_applied'] == df['promo_code_used']).all()
Drop = df.drop('promo_code_used', axis=1)
print(Drop.columns)


#Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"          
password = "abhay123"         
host = "localhost"            
port = "5432"                 
database = "customer_behavior"
# Create the connection engine
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
#Load DataFrame into PostgreSQL
table_name = "customer"  # choose any table name
# Upload DataFrame to PostgreSQL
df.to_sql(table_name, engine, if_exists='replace', index=False)
# Step 4: Confirmation message
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")

