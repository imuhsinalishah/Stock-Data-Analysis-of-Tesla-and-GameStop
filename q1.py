import yfinance as yf

# Extract Tesla stock data
tesla_data = yf.download('TSLA', start='2020-01-01', end='2024-01-01')

# Reset the index
tesla_data_reset = tesla_data.reset_index()

# Display the first five rows
print(tesla_data_reset.head())
