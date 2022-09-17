import reference
import pandas as pd

key = '8Y1nvUm3DsC4y36_ofpn'
ticker = 'AAPL'
limit = '10'

api_url : f'https://data.nasdaq.com/api/v3/datasets/{ticker}/ORB.csv?api_key={key}'

data = requests.get(api_url).json()
df = pd.dataframe(data['results'])

#transpose dataframe so that keys are row names
statement = df.T

#find data over a given period