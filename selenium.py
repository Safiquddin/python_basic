from selenium import webdriver
from selenium.webdriver.common.utils import keys_to_typing
from webdriver_manager.chrome import ChromeDriverManager
import time
class GoogleSearch:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://google.co.in')
    # driver.maximize_window()
    # driver.find_element_by_xpath("//input[@name='Mahesh']")
    # time.sleep(5)
    # driver.find_element_by_css_selector('input.lsb').click()
    # driver.find_element_by_link_text('Mahesh Babu - Wikipedia').click()
    driver.maximize_window()
    time.sleep(5)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("Elon Musk")
    inputElement.submit()
    inputElement.find_element_by_link_text('Elon Musk - Wikipedia').click()

gs=GoogleSearch()
gs.chrome()


    
    
   # driver=webdriver.Chrome("C:\chromedriver.exe")
   # from selenium.webdriver.firefox.webdriver import WebDriver