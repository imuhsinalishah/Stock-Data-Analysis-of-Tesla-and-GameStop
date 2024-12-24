# Extract GameStop stock data
gme_data = yf.download('GME', start='2020-01-01', end='2024-01-01')

# Reset the index
gme_data_reset = gme_data.reset_index()

# Display the first five rows
print(gme_data_reset.head())
