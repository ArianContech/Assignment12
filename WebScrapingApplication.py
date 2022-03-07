import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

PriceArr = []
PriceChangeArr = []
PriceChangePercentArr = []

# Change This Address To your Proper Address and in windows use / instead of \ like "c:/uni/arian/FinancialData.csv"
csvPath = 'F:/University/Tools & Techniques for Data Science/Day7/Assignment12/FinancialData.csv'

# we need to Set a Loop for get data permanently
while(True):
#for a in range(0, 100):
   html = requests.get('https://markets.businessinsider.com/currencies/btc-usd/')
   soup = BeautifulSoup(html.content, 'html.parser')
   Price = soup.find('span', {'class': 'price-section__current-value'})
   PriceChange = soup.find('span', {'class': 'price-section__absolute-value'})
   PriceChangePercent = soup.find('span', {'class': 'price-section__relative-value'})

   # Print scraped data to Terminal
   print("BTC Price      : ", Price.text)
   print("BTC Change     : ", PriceChange.text)
   print("Change Persent : ",PriceChangePercent.text)
   print("-------------")

   PriceArr.append(Price.text)
   PriceChangeArr.append(PriceChange.text)
   PriceChangePercentArr.append(PriceChangePercent.text)

   ExtractData = {
      'Bitcoin Price': PriceArr,
      'PriceChange': PriceChangeArr,
      'PriceChangePercent': PriceChangePercentArr
   }

   # Write scraped data to Csv File
   try:
      df = pd.DataFrame(ExtractData)
      df.to_csv(csvPath, index=False, encoding='utf-8')
   except:
      print("We cant Save Data to csv.change csv Path")

   # scraping data interval
   time.sleep(5)
