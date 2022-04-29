from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from Tests.pages.mainPage import MainPage
# from Tests.pages.aboutPage import AboutPage


# Chrome driver path
s = Service('C:\\Program Files (x86)\\chromedriver.exe')

# create webdriver object
driver = webdriver.Chrome(service=s)


def test_mainPage_textFields():

    main = MainPage(driver)

    main.enter_motorKV('2400')
    main.enter_battVolt('16.8')
    main.enter_spur('18')
    main.enter_pinion('54')
    main.enter_fgr('3.92')
    main.enter_wheelRadius('2.25')
    time.sleep(1)
    main.click_calculate()


def test_input():
    assert driver.find_element(By.ID, 'motorkV') == '2400'







# fetch browser instance
# #driver.get('https://rcspeedestimator.herokuapp.com/')
#driver.get('http://127.0.0.1:5000/')


'''# text_field id's = motorKV, battVolt, pinion, spur, fgr, wheelradius, submit-value=calculate
driver.find_element(By.ID, 'motorkV').send_keys('2400')

driver.find_element(By.ID, 'battVolt').send_keys('16.8')

driver.find_element(By.ID, 'pinion').send_keys('18')

driver.find_element(By.ID, 'spur').send_keys('50')

driver.find_element(By.ID, 'fgr').send_keys('3.92')

driver.find_element(By.ID, 'wheelradius').send_keys('2.75')

# find the resulting speed from calculation that is displayed upon clicking 'calculate'
calculated_speed = driver.find_element(By.CLASS_NAME, 'calculated').get_attribute('innerText')'''

'''if __name__ == '__main__':
    if __name__ == '__main__':
        pytest'''
