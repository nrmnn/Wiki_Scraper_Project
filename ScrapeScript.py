import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Morgan_Freeman'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title> Morgan_Freeman_Wiki_Scrapper </title>
</head>
<body>
    <h1> Morgan Freeman </h1>
    <img src="{}"> </img>
    <p> 
    <b> Born: </b> {} <br/>
    <b> Education: </b> {} <br/>
    <b> Occupations: </b> {} <br/>
    <b> Organization: </b> {} <br/>
    <b> Works: </b> {} <br/>
    <b> Spouses: </b> {} <br/>
    <b> Children: </b> {} <br/>
    <b> Awards: </b> {} <br/>
    </p>
</body>
</html>
'''

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the class 'infobox vcard'
infobox = soup.find('table', {'class': 'infobox biography vcard'})

# Find the image element within the infobox element
img = infobox.find('img')

# Extract the src attribute of the image element
#img_src = img['src']
	
img_url = 'https:' + img['src']

# Find the rows in the table
rows = infobox.find_all('tr')

# Loop through the rows and extract the personal information
personal_info = {}
for row in rows:
    # Check if the row contains personal information
    if row.th and row.th.text in ['Born', 'Education', 'Occupations', 'Years active', 'Organization', 'Works', 'Spouses', 'Children', 'Awards']:
        key = row.th.text.strip()
        value = row.td.text.strip()
        personal_info[key] = value

# Remove '\n' and '\u200b' from string values
for key in personal_info:
    personal_info[key] = personal_info[key].replace('\n', '').replace('\u200b', '').replace('\xa0', '')

with open('index.html', 'w', encoding='utf-8') as f:
    html = HTML_TEMPLATE.format(img_url, personal_info['Born'], personal_info['Education'], personal_info['Occupations'], personal_info['Organization'], personal_info['Works'], personal_info['Spouses'], personal_info['Children'], personal_info['Awards'])
    f.write(html)

#with open('Morgan_Freeman_Wiki.html', 'w', encoding='utf-8') as f:
 #   html = HTML_TEMPLATE.format(img_url, personal_info['Born'], personal_info['Occupations'], personal_info['Organization'], personal_info['Works'], personal_info['Spouses'], personal_info['Children'], personal_info['Awards'])
  #  f.write(html)