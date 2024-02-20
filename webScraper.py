!pip install selenium

!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import sqlite3
import traceback
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')



driver = webdriver.Chrome(options=chrome_options)

try:
  driver.get('https://finance.yahoo.com/trending-tickers')

  css_selector="button.carousel-btn[title='next']"
  WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector))
  )
  button = driver.find_element(By.CSS_SELECTOR,css_selector)
  button.click()

  # time.sleep(10)

  element_id= "mrt-node-Lead-2-FinanceHeader"
  WebDriverWait(driver,10).until(
      EC.presence_of_all_elements_located((By.ID,element_id))
  )

  element = driver.find_element(By.ID,element_id)
  data=element.get_attribute('textContent')
  crude_oil_pattern=r"Crude Oil(\d+.\d+)"
  gold_pattern= r"Gold(\d+,\d+.\d+)"
  silver_pattern= r"Silver(\d+.\d+)"

  crude_oil_rate= re.search(crude_oil_pattern,data)
  gold_rate=re.search(gold_pattern,data)
  silver_rate = re.search(silver_pattern,data)

  rates_to_write="Crude Oil Rate: {}\n Gold Rate: {}\n Silver Rate: {}\n".format(
      crude_oil_rate.group(1) if crude_oil_rate else "Not Found",
      gold_rate.group(1) if gold_rate else "Not Found",
      silver_rate.group(1) if silver_rate else "Not Found"
  )

  with open('commodity_prices.txt','w')as file:
    file.write(rates_to_write)

  conn= sqlite3.connect('CommodityDatabase.db')
  c= conn.cursor()
  c.execute('''DROP TABLE IF EXISTS commodityTable''')
  c.execute('''CREATE TABLE IF NOT EXISTS CommodityTable
               (id INTEGER PRIMARY KEY, crude_oil TEXT, gold TEXT, silver TEXT)''')

  c.execute('''INSERT INTO CommodityTable (crude_oil,gold,silver) VALUES(?,?,?) ''',
            (crude_oil_rate.group(1) if crude_oil_rate else "Not Found",
             gold_rate.group(1) if gold_rate else "Not Found",
             silver_rate.group(1) if silver_rate else "Not Found"))


  conn.commit()
  conn= sqlite3.connect('CommodityDatabase.db')
  c= conn.cursor()
  c.execute('''SELECT * from CommodityTable ''')

  columns = [description[0] for description in c.description]

  print("\t".join(columns))


  rows=c.fetchall()

  for row in rows:
    print("\t".join(map(str,row)))
  conn.close()

except Exception as e:
  print("Error: ",e)
  traceback.print_exc()

finally:
  driver.quit()