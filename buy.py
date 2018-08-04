from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, yaml

url = "https://www.google.com/"

def read_config(filepath):
    with open(filepath, 'r') as stream:
            return yaml.load(stream)

def buy(config):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    # login
    print("login...")
    driver.get("https://www.rakuten.com.tw")
    driver.find_element_by_id("auto_sign_in").click()
    driver.find_element_by_id("form:userId").click()
    driver.find_element_by_id("form:userId").clear()
    driver.find_element_by_id("form:userId").send_keys(config['login']['email'])
    driver.find_element_by_id("form:password").clear()
    driver.find_element_by_id("form:password").send_keys(config['login']['password'])
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='隱私權政策'])[1]/following::span[1]").click()

    # click item
    print("go to item page...")
    driver.get(config['page'])
    #driver.find_element_by_id("auto_variant-label-0-0").click()
    
    # click buy
    print("click buy...")
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='數量：'])[1]/following::i[1]").click()
    #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='數量：'])[1]/following::span[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='詳細資料'])[2]/following::button[1]").click()
    
    # step 1 type address and personal info
    print("filling address and personal info...")
    driver.find_element_by_name("recipient[province]").click()
    Select(driver.find_element_by_name("recipient[province]")).select_by_visible_text(config['buy']['province'])
    driver.find_element_by_name("recipient[city]").click()
    Select(driver.find_element_by_name("recipient[city]")).select_by_visible_text(config['buy']['city'])
    driver.find_element_by_name("recipient[address1]").click()
    driver.find_element_by_name("recipient[address1]").clear()
    driver.find_element_by_name("recipient[address1]").send_keys(config['buy']['address'])
    driver.find_element_by_id("telephone").clear()
    driver.find_element_by_id("telephone").send_keys(config['buy']['phone'])
    # click submit
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Shopping is Entertainment!'])[1]/preceding::button[1]").click()
    
    # step 2 type payment info
    print("filling payment info...")
    driver.find_element_by_name("payment-methods-selection").click()
    print("paying...")
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='確認結帳'])[1]/following::div[1]").click()

    print('finish...')

if __name__ == '__main__':
    config = read_config('config.yml')
    buy(config)
