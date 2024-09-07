import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

# Reading the CSV file and setting 'Date' as the index
df = pd.read_csv("Price.csv", index_col="Date", parse_dates=True)

# Basic financial statistics
print(df.describe())

# Cleaning and converting 'Close' column to float
df["Close"] = df['Close'].str.replace(',', '').astype(float)

# Calculating rolling averages
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA10"] = df["Close"].rolling(window=10).mean()

# Calculating daily returns
df["Returns"] = df["Close"].pct_change()

# Print the dataframe to inspect
print(df)

# Plotting
pl.figure(figsize=(12, 6))

# Plot stock price and moving averages
pl.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
pl.plot(df["Close"], color="r", label="Close Price")
pl.plot(df["MA5"], color="b", label="5-Day MA")
pl.plot(df["MA10"], color="yellow", label="10-Day MA")
pl.title("Stock Price and Moving Averages")
pl.xlabel("Date")
pl.ylabel("Price")
pl.legend(loc='upper left')
pl.xticks(rotation=45)

# Plot daily returns
pl.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
pl.plot(df["Returns"], color="green", label="Daily Returns")
pl.title("Daily Returns")
pl.xlabel("Date")
pl.ylabel("Returns")
pl.legend(loc='upper left')
pl.xticks(rotation=45)

pl.tight_layout()
pl.show()


