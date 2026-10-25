<img width="745" height="416" alt="Screenshot 2026-10-25 093938" src="https://github.com/user-attachments/assets/c543d291-c94a-4796-9ad3-91a081cd0743" /># 
📚 Book Market Analysis Dashboard

An end-to-end data analytics project: I scraped 1,000 books from a website,
cleaned the data with Python, analyzed it with pandas, and built an
interactive dashboard in Power BI.

<img width="740" height="418" alt="Screenshot 2026-10-25 100858" src="https://github.com/user-attachments/assets/05418ee3-62ef-4601-92d2-2c9bd9db01b7" />


## 🎯 Project Goal

To understand how book prices and ratings vary across categories, and to
find out whether higher-priced books get better ratings.

## 🔍 Key Findings

- **19.6%** of books are rated 5 stars, and ratings are spread
  evenly across all five levels.
- **Travel** is the most expensive category, with an average
  price of **£39.79**.
- **Sequential-Art** has the most books (75 titles).
- The correlation between price and rating is **0.02816**, which means
  **price does not predict rating**.
- Many categories lies at Avg rating of **3** and at the Avg price of **£30 - £40**.  

## 🛠️ Tools Used

| Step | Tool |
|---|---|
| Web scraping | Python, requests, BeautifulSoup |
| Data cleaning & analysis | Python, pandas, matplotlib |
| Dashboard | Power BI Desktop, DAX |
| Version control | Git & GitHub |

## 📂 Project Structure

```
book-market-analysis/
├── scraper.py            # collects data from the website
├── cleaning.ipynb        # cleans the raw data
├── analysis.ipynb        # answers business questions
├── dashboard/
│   ├── book_dashboard.pbix
│   └── dashboard_screenshot.png
├── data/
│   ├── raw_books.csv
│   └── clean_books.csv
└── requirements.txt
```

## ⚙️ How the Project Works

1. **Collect:** `scraper.py` visits every category on
   books.toscrape.com and saves title, price, rating and category.
2. **Clean:** I converted prices like `£51.77` to numbers, turned rating
   words into numbers (Three → 3), removed duplicates, and created price bands.
3. **Analyze:** I used pandas `groupby` to compare categories and
   calculated the price-rating correlation.
4. **Visualize:** I built a Power BI dashboard with KPI cards, charts
   and slicers, using DAX measures.

## ▶️ How to Run

```bash
pip install -r requirements.txt
python scraper.py
```

Then open the notebooks in order, and open
`dashboard/book_dashboard.pbix` in Power BI Desktop.

## 📌 Notes

- Data comes from [books.toscrape.com](https://books.toscrape.com),
  a site built for practicing web scraping.
- The data is fictional, so the findings are about this dataset, not
  the real book market.
