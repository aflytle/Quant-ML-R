import reference
import pandas as pd

api = 'xQpCFLsVH5XDFMEee3QF2Bh3AEa5VkJi'
ticker = 'AAPL'
limit = '10'

api_url : f'https://api.polygon.io/vX/reference/financials?ticker={ticker}&apiKey={api}'

data = requests.get(api_url).json()
df = pd.dataframe(data['results'])

#transpose dataframe so that keys are row names
statement = df.T

#find data over a given period