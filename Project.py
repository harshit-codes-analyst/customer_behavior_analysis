import pandas as pd

# Step 1: Load the CSV file (use forward slash for clean path)
df = pd.read_csv('C:/Users/Harshit Tiwari/OneDrive/Desktop/Project Data/customer_shopping_behavior.csv')

# Step 2: Clean column names (remove hidden spaces)
df.columns = df.columns.str.strip()

# Step 3: Drop duplicate 'Review_Rating' column if it exists
if 'Review_Rating' in df.columns:
    df.drop(columns=['Review_Rating'], inplace=True)

# Step 4: Fill missing values in 'Review Rating' group-wise by Category
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

# Step 5: Rename column to consistent style (optional but cleaner)
df.rename(columns={'Review Rating': 'Review_Rating'}, inplace=True)

# Step 6: Print outputs to verify
print("\n----- First 5 Rows -----")
print(df.head())

print("\n----- Info -----")
print(df.info())

print("\n----- Summary -----")
print(df.describe(include='all'))

print("\n----- Missing Values After Cleaning -----")
print(df.isnull().sum())

print("\n----- Check Missing in Review_Rating -----")
print("Missing in Review_Rating column:", df['Review_Rating'].isna().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')

df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels = labels)
print(labels)

df[['age','age_group']].head(10)
print(df)

frequency_mapping = {
  'Fortnightly':14,
  'Weekly':7,
  'Monthly':30,
  'Quarterly':90,
  'Bi-weekly':14,
  'Annually':365,
  'Every 3 Months':90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(frequency_mapping)

df[['purchase_frequency_days','frequency_of_purchases']]
print(df.head(10))

print(df[['discount_applied', 'promo_code_used']].head(10))
df = df.drop('promo_code_used',axis=1)

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"         # default user
password = "harshit"         # the password you set during installation
host = "localhost"            # if running locally
port = "5432"                 # default PostgreSQL port
database = "customer_behavior"  # the database you created in pgAdmin

from sqlalchemy import create_engine

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"        # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
