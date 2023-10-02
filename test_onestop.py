# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOnestop():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_onestop(self):
    # Test name: onestop
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.facebook.com/")
    # 2 | setWindowSize | 1024x737 | 
    self.driver.set_window_size(1024, 737)
    # 3 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 4 | type | id=email | safiquddinkhan@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("safiquddinkhan@gmail.com")
    # 5 | click | id=pass | 
    self.driver.find_element(By.ID, "pass").click()
    # 6 | type | id=pass | s3q.k2n@1236
    self.driver.find_element(By.ID, "pass").send_keys("$password")
    # 7 | click | id=u_0_d_K/ | 
    self.driver.find_element(By.ID, "u_0_d_K/").click()
    # 8 | click | css=.bp9cbjyn:nth-child(2) > .tojvnm2t .a8c37x1j | 
    self.driver.find_element(By.CSS_SELECTOR, ".bp9cbjyn:nth-child(2) > .tojvnm2t .a8c37x1j").click()
    # 9 | close |  | 
    self.driver.close()
  