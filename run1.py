# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:04:33 2021

@author: F ANAME
"""
# pip install webdriver-manager
import os

os.environ['DISPLAY'] = ':0'

import html5lib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#############################################################################

username = "modirimasilela567@gmail.com"
password = "0000123987@Tj"

getdriver = ("https://bot.binary.com/bot.html#")


# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)



#driver = webdriver.Chrome()                 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(getdriver)



time.sleep(5)

pyautogui.press('f11')

time.sleep(10)

# Click popup
js = 'response = document.getElementsByClassName("button-secondary")[0].click();'
driver.execute_script(js)

time.sleep(3)

# Click login
js = 'login = document.getElementById("login").click();'
driver.execute_script(js)


time.sleep(3)

#send login details
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/form/div[1]/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/form/div[2]/input").send_keys(password)

time.sleep(1)

# Click login
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/form/div[3]/button").click()

time.sleep(20)

#Click want to upload file button
driver.find_element_by_xpath("/html/body/div[8]/button[2]").click()

time.sleep(2)

#Click load 
driver.find_element_by_xpath("/html/body/div[14]/div[2]/form/div[2]/button").click()

time.sleep(3)

# driver.find_element_by_xpath("/html/body/div[14]/div[2]/form/div[2]/button").send_keys("C:/Users/F ANAME/Downloads/AKANI WEALTH PHONE 2.5.xm")

# Send file path
pyautogui.write('C:\\Users\\F ANAME\\Downloads\\AKANI WEALTH PHONE 2.5.xml') 
pyautogui.press('enter')


time.sleep(3)

driver.find_element_by_xpath("/html/body/div[8]/button[12]").click()


























