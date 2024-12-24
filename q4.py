# URL with GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

# Send a GET request to fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract revenue data from the table (adjust selectors as needed)
table = soup.find('table', {'class': 'historical_data_table'})
rows = table.find_all('tr')

# Parse the table into a DataFrame
data = []
for row in rows[1:]:
    columns = row.find_all('td')
    year = columns[0].text.strip()
    revenue = columns[1].text.strip()
    data.append([year, revenue])

# Create DataFrame
gme_revenue = pd.DataFrame(data, columns=['Year', 'Revenue'])

# Display last 5 rows
print(gme_revenue.tail())
