import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\clean_books.csv")

#Analysis
#Question 1: What is the overall picture?
#Headline numbers to be shown as KPI in PowerBI Dashboard
print("Total books:",len(df))
print("Average price: £", round(df["price"].mean(), 2))
print("Cheapest: £", df["price"].min())
print("Most Expensive: £", df["price"].max())
print("Average rating:", round(df["rating"].mean(), 2))


#Question 2: Which categories have the most books?
cat_counts = df["category"].value_counts().head(10)
print(cat_counts)

cat_counts.plot(kind = "barh", title="Top 10 categories by Number of Books")
plt.xlabel("Number of Books")
plt.gca().invert_yaxis()        #Biggest bar on top
plt.savefig("Number of books.png", bbox_inches= "tight")
plt.show()

#Question 3: Which categories are the most expensive?
price_by_cat = df.groupby("category").agg(
    avg_price = ("price","mean"),
    book_count = ("title", "count")
)
big = price_by_cat[price_by_cat["book_count"] >= 10]
print(big.sort_values("avg_price", ascending=False).head(10).round(2))

price_by_cat.head(10).plot(kind="barh", title= "Most expensive categories (Avg Price)")
plt.xlabel("Average Price (£)")
plt.gca().invert_yaxis()
plt.savefig("Expensive caregories.png", bbox_inches= "tight")
plt.show()

#Question 4: Which categories are rated best?
rating_by_cat = df.groupby("category").agg(
    avg_rating = ("rating","mean"),
    book_count = ("title", "count")
)

#Keep only categories with at least 10 books to ignore small categories,
#Which can akter the results with only 1/2 datas
big = rating_by_cat[rating_by_cat["book_count"] >= 10]
print(big.sort_values("avg_rating", ascending=False).head(10))

#Question 5: Do expensive books get better results?
print("The correlation of Price and Rating is:", df["price"].corr(df["rating"]))

plt.scatter(df["price"],df["rating"], alpha = 0.3)
plt.xlabel("Price ()")
plt.xlabel("Price (£)")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.savefig("price_Rating.png", bbox_inches= "tight")
plt.show()

#Question 6: What percentage of books are 5 star?
five_star = df[df["rating"]==5]
perc_star = len(five_star) / len(df) * 100
print(round(perc_star, 2), "% of books are 5 stars")
