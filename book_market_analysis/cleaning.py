import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw_books.csv")
print(df.shape)

#Step 1: Inspect the data
df.head()               #shows the first 5 rows of the dataframe
df.info()               #column names, data types, and non-null counts
df.isnull().sum()       #shows the number of missing values in each column
df.duplicated().sum()   #shows the number of duplicate rows in the dataframe

#Step 2: Clean the data
#clean the price column by removing the currency symbol and converting it to a float
df["price"] = df["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

#step 3: Clean the rating column by converting the text to a numerical value
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["rating"] = df["rating"].map(rating_map)

#step 4: Clean text and remove duplicates
df["title"] = df["title"].str.strip()  #remove leading and trailing whitespace
df["category"] = df["category"].str.strip()  #remove leading and trailing whitespace

print("Duplicates before cleaning:", df.duplicated().sum())
df = df.drop_duplicates()  #remove duplicate rows
print("Rows after:", len(df))

#step 5: Creating useful new columns
#Group prices into bands
df["price_band"] = pd.cut(
    df["price"],
    bins = [0, 20,40, 60],
    labels = ["Budget (under £20)", "Mid (£20 - £40)", "Premium (£40+)"]
)

#Readable ratings label
df["rating_label"] = df["rating"].astype(str) + " Star"

#Step 6: Final check and save
df.info()
print(df["rating"].unique())    #Should show only numbers from 1 to 5
print(df["price"].describe())   #min, max, avg

df.to_csv("data/clean_books.csv", index=False)