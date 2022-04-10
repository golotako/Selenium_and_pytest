# Selenium Webdriver

'''
writer notes:
If you want change the sleep.time to less seconds
'''

# Importing the libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Opening the browser
driver = webdriver.Chrome(r"C:\Users\eviyt\OneDrive\Desktop\DEVOPS\chromedriver_win32\chromedriver.exe")

#max window
driver.maximize_window()


# Opening the youtube website
driver.get("https://www.youtube.com/")
time.sleep(20)

# Searching for the video
search = driver.find_element_by_name('search_query')
search.send_keys("tell me why broklyn 99")
search.send_keys(Keys.ENTER)
time.sleep(10)

# click on the first video
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
time.sleep(20)

# click on like button
like_btn = driver.find_element_by_xpath('//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a')
like_btn.click()
time.sleep(15)

#close the browser

driver.close()
