import matplotlib.pyplot as plt

def make_graph(stock_data):
    plt.figure(figsize=(10,5))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Closing Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title('Tesla Stock Price Over Time')
    plt.legend()
    plt.show()

# Call the function with Tesla data
make_graph(tesla_data_reset)
