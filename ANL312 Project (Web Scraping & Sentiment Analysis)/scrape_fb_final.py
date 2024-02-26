import requests
import re
import json
import time
import collections
from bs4 import BeautifulSoup

import csv
import pandas as pd

from credentials import username, password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

payload = {'email': username, 'pass': password} # FaceBook username and password
grab_url = 'https://mobile.facebook.com/pg/Grab/community/?ref=page_internal&mt_nav=0'

class FaceBookBot():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome('../../../chromedriver', options=options)

    def login(self, username, password):
        self.driver.get("https://mobile.facebook.com/login")

        time.sleep(5)

        email_in = self.driver.find_element_by_xpath('//*[@id="m_login_email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="m_login_password"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@name="login"]')
        login_btn.click()

        time.sleep(5)

bot = FaceBookBot()
bot.login(payload['email'], payload['pass'])

bot.driver.get(grab_url)

time.sleep(3)

for i in range(1, 200):
    bot.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)

    if i % 10 == 0:
        print(f'{i} times scrolled.')

page = bot.driver.page_source
soup = BeautifulSoup(page, 'html.parser')

contents = soup.find_all('span', attrs={'data-sigil': 'more'})

posts_contents = []
for posts in contents:
    posts_contents.append(posts.text)

print(f'{len(posts_contents)} reviews collected.')

df = pd.DataFrame(data={'grab_reviews': posts_contents})
df.to_csv('grab_reviews.csv', index=False)
