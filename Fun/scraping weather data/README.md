# Scraping Weather Data (Requests and BeautifulSoup)

Data obtained on the night of 18 August 2020.

Information obtained: Weather and temperature forecast for the next 10 days (until 1 Sep)

```python
# The Weather Channel
page_wc = requests.get('https://weather.com/en-SG/weather/tenday/l/6d0896fdc9c5b15f33121e83b62e4094e3c07f495ba1a6e56c9e5f29090c4f21#detailIndex5')
soup_wc = BeautifulSoup(page_wc.content, 'html.parser')

ten_day = soup_wc.find(class_='_-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS')
forecast_items_wc = ten_day.find_all(class_='_-_-components-src-atom-Disclosure-Disclosure--themeList--1Dz21')

tonight_wc = forecast_items_wc[0]

period_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--daypartName--3emSU').get_text()
print(f'Period: {period_wc}')
temp_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--temp--1s3a7').get_text()
print(f'Temp: {temp_wc}')
short_desc_wc = tonight_wc.find(class_='_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--narrative--3Ti6_').get_text()
print(f'Short desc: {short_desc_wc}')

period_tags_wc = ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--daypartName--3emSU')
periods_wc = [pt.get_text() for pt in period_tags_wc]
short_descs_wc = [sd.get_text() for sd in ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--narrative--3Ti6_')]
temps_wc = [t.get_text() for t in ten_day.select('._-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--temp--1s3a7')]

weather_wc_df = pd.DataFrame({'period': periods_wc,
                              'temp': temps_wc,
                              'short_desc': short_descs_wc})
```

The scrapped temperature data had the degree character included. As such, cleaning is needed to remove the character and convert the data type to integer.

```python
weather_wc_df['temp_int'] = weather_wc_df.temp.apply(lambda x:x.replace(u"\u00b0", '')).astype('int')
weather_wc_df['date'], weather_wc_df['period_'] = weather_wc_df['period'].str.split('|', 1).str
weather_wc_df['period_'] = weather_wc_df['period_'].apply(lambda x:x.replace(' ', '')) # remove the extra space before 'Night' and 'Day'

weather_wc = weather_wc_df[['date', 'period_', 'temp_int', 'short_desc']]
print(weather_wc.head())
```

![weather_wc.head()](https://github.com/ezhentan/projectsrepo/blob/master/Fun/scraping%20weather%20data/Screenshot%202020-08-18%20at%2011.00.50%20PM.png)

Mean day temperature: 30.36
<br>
Mean night temperature: 26.47

# References

1. BeautifulSoup tutorial: https://www.dataquest.io/blog/web-scraping-tutorial-python/
2. Webpage scrapped: https://weather.com/en-SG/weather/tenday/l/6d0896fdc9c5b15f33121e83b62e4094e3c07f495ba1a6e56c9e5f29090c4f21#detailIndex5
