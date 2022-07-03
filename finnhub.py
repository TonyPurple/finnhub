import requests
import json
from pprint import pprint
import csv

token = "cb0ssoqad3idnllqhtr0"
symbol = "AAPL"
symbol1 = "AMZN"
symbol2 = "NFLX"
symbol3 = "META"
symbol4 = "GOOGL"

base_url = "https://finnhub.io/api/v1/quote?"
r = requests.get(base_url, params = {'symbol':symbol,'token':token})
r1 = requests.get(base_url, params = {'symbol':symbol1,'token':token})
r2 = requests.get(base_url, params = {'symbol':symbol2,'token':token})
r3 = requests.get(base_url, params = {'symbol':symbol3,'token':token})
r4 = requests.get(base_url, params = {'symbol':symbol4,'token':token})
text = r.text
text1 = r1.text
text2 = r2.text
text3 = r3.text
text4 = r4.text
company_quote = json.loads(text)
company_quote1 = json.loads(text1)
company_quote2 = json.loads(text2)
company_quote3 = json.loads(text3)
company_quote4 = json.loads(text4)

pprint(company_quote['dp'])
pprint(company_quote['c'])
pprint(company_quote['pc'])
pprint(company_quote1['dp'])
pprint(company_quote1['c'])
pprint(company_quote1['pc'])
pprint(company_quote2['dp'])
pprint(company_quote2['c'])
pprint(company_quote2['pc'])
pprint(company_quote3['dp'])
pprint(company_quote3['c'])
pprint(company_quote3['pc'])
pprint(company_quote4['dp'])
pprint(company_quote4['c'])
pprint(company_quote4['pc'])

most_volatile_stock = company_quote1

header = ['stock_symbol', 'percentage_change', 'current_price', 'last_close_price']
data = ['AMZN', 3.1541, 109.56, 106.21]

with open('most_volatile_stock.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)