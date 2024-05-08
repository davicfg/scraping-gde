# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# put the links in this array
gdes = ["https://developers.google.com/profile/u/XXXX", "https://developers.google.com/profile/u/AAAA", "https://developers.google.com/profile/u/BBBB"]


for gde in gdes:
  driver.get(gde)
  line = ""
  time.sleep(6)

  line += driver.find_element(By.CSS_SELECTOR, '.profile-name > h2').text
  line +="|"

  line += gde
  line +="|"

  links = driver.find_elements(By.XPATH, "//div[@class='profile-links']/div")

  for link in links:
    line+=link.find_element(By.TAG_NAME, 'a').get_attribute('href')
    line +="|"

  print(line)

driver.close()