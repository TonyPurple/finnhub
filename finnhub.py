import requests
import json
from pprint import pprint

token = "cb0ssoqad3idnllqhtr0"
symbol = "AAPL"

base_url = "https://finnhub.io/api/v1/stock/profile2?"
r = requests.get(base_url, params = {'symbol':symbol,'token':token})
text = r.text
company_profile = json.loads(text)

pprint(company_profile)