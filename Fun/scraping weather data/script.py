import requests
from bs4 import BeautifulSoup
import pandas as pd

# The Weather Channel
page_wc = requests.get('https://weather.com/en-SG/weather/tenday/l/6d0896fdc9c5b15f33121e83b62e4094e3c07f495ba1a6e56c9e5f29090c4f21#detailIndex5')
soup_wc = BeautifulSoup(page_wc.content, 'html.parser')

ten_day = soup_wc.find(class_='_-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS')
print(ten_day)
forecast_items_wc = ten_day.find_all(class_='_-_-components-src-atom-Disclosure-Disclosure--themeList--1Dz21')
print(forecast_items_wc)
print(len(forecast_items_wc))

print()

tonight_wc = forecast_items_wc[0]

period_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--daypartName--3emSU').get_text()
print(f'Period: {period_wc}')
temp_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--temp--1s3a7').get_text()
print(f'Temp: {temp_wc}')
short_desc_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--narrative--3Ti6_').get_text()
print(f'Short desc: {short_desc_wc}')

print()

period_tags_wc = ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--daypartName--3emSU')
periods_wc = [pt.get_text() for pt in period_tags_wc]
short_descs_wc = [sd.get_text() for sd in ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--narrative--3Ti6_')]
temps_wc = [t.get_text() for t in ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--temp--1s3a7')]

print(periods_wc)
print(short_descs_wc)
print(temps_wc)

print(len(periods_wc), len(temps_wc), len(short_descs_wc))

weather_wc_df = pd.DataFrame({'period': periods_wc,
                              'temp': temps_wc,
                              'short_desc': short_descs_wc})

print(weather_wc_df.head())
print(len(weather_wc_df))

print(weather_wc_df.info())

print()

weather_wc_df['temp_int'] = weather_wc_df.temp.apply(lambda x:x.replace(u"\u00b0", '')).astype('int')
print(weather_wc_df.head(2))
# print(weather_wc_df.info())

weather_wc_df['date'], weather_wc_df['period_'] = weather_wc_df['period'].str.split('|', 1).str
weather_wc_df['period_'] = weather_wc_df['period_'].apply(lambda x:x.replace(' ', ''))
print(weather_wc_df.head(2))

print()

weather_wc = weather_wc_df[['date', 'period_', 'temp_int', 'short_desc']]
print(weather_wc.head())

print()

print(weather_wc[weather_wc['period_'] == 'Night']['temp_int'].mean())
print(weather_wc[weather_wc['period_'] == 'Day']['temp_int'].mean())
