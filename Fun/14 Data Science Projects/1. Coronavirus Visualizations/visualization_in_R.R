r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

install.packages('plotly')
library(plotly)

library(dplyr)
library(readr)

## Import data
df <- read_csv('content/post/covid_19_data.csv', col_types='dccccddd')

## Rename columns
#names(df)[names(df)=='Country/Region'] <- 'Country'
#names(df)[names(df)=='ObservationDate'] <- 'Date'
df <- rename(df, Country='Country/Region', Date=ObservationDate)
df

## Manipulate dataframe
df_countries <- df %>%
  group_by(Country, Date) %>%
  summarise(Confirmed = sum(Confirmed))
#df_countries

df_countries <- arrange(df_countries, desc(Date))
df_countries <- distinct(df_countries, Country, .keep_all=TRUE)
df_countries <- filter(df_countries, Confirmed > 0)
df_countries

## Creating the static chart
g <- list(showframe=FALSE,
          showcoastlines=FALSE,
          projection=list(type='equirectangular'))

fig <- plot_ly(df_countries, type='choropleth', locations=df_countries$Country, locationmode='country names',
               z=df_countries$Confirmed, color=df_countries$Confirmed, colorscale='Reds',
               marker=list(line=list(color='black', width=0.5)))

fig <- fig %>% 
  layout(title=list(text='Confirmed Cases as of September 23, 2020')) %>%
  layout(geo=g)

fig
