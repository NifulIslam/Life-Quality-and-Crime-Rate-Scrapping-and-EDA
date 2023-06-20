import pandas as pd
life_quality=pd.read_csv('life_quality_2023.csv')
crime_reate=pd.read_csv('crime_rate_2023.csv')
df = pd.merge(life_quality, crime_reate, on=['Country'])
df.rename(columns={'Total':'total life quality', 'Rank':'Crime Rank'}, inplace=True)
df.to_csv("data.csv",index=False)
