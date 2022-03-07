    # Objective: build 2 web scrapers to choose different websites (use variables) accurately grab a certain text in html.  
    # must able scrape infos from web
    # must able to change website 
    # must able save & export data
    # must able to format data (remove html tags and normalize data)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe" # set the path to chromedriver
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/") #scrape from YouTube
print(driver.title)

    # Selenium will wait for a maximum of 10 seconds for an element matching the given criteria to be found. 
    # If no element is found in that time, a TimeoutException is thrown.
    # By default, WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success.

time.sleep(5)
search = driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string')

print(search)
# main = driver.find_element_by_id()

driver.close()

print("Test Completed Successfully")