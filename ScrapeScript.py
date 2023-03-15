import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Morgan_Freeman'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the class 'infobox vcard'
infobox = soup.find('table', {'class': 'infobox biography vcard'})


# Find the rows in the table
rows = infobox.find_all('tr')

breakpoint()

# Loop through the rows and extract the personal information
personal_info = {}
for row in rows:
    # Check if the row contains personal information
    if row.th and row.th.text in ['Born', 'Education', 'Occupations', 'Years active', 'Organization', 'Works', 'Spouses', 'Children', 'Awards']:
        key = row.th.text.strip()
        value = row.td.text.strip()
        personal_info[key] = value

# Print the personal information
print(personal_info)