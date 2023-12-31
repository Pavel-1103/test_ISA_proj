import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_get_form_login():
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.implicitly_wait(5)

    try:
        browser.get("https://solmar.com.ua/ua/")
        item_account_button = browser.find_element(By.XPATH, "//a[@class='s-header__item-icon']//parent::div[@class='s-header__item -account']")
        item_account_button.click()
        time.sleep(2)

        email_field = browser.find_element(By.XPATH, "//input[@name='USER_LOGIN']")
        email_field.send_keys("wohocid569@qianhost.com")
        time.sleep(3)

        password_field = browser.find_element(By.XPATH, "//input[@name='USER_PASSWORD']")
        password_field.send_keys("Qwerty123456")
        time.sleep(3)

        login_button = browser.find_element(By.XPATH, "//input[@value='Увійти']")
        login_button.click()

        message = WebDriverWait(browser, 5).until_not(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='s-modal__inner done']"))
        )
        time.sleep(10)
    
    finally:
        browser.quit()
        print("Browser quit")


def test_exit_from_account():
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.implicitly_wait(5)

    try:
        browser.get("https://solmar.com.ua/ua/")
        item_account_button = browser.find_element(By.XPATH, "//a[@class='s-header__item-icon']//parent::div[@class='s-header__item -account']")
        item_account_button.click()
        time.sleep(2)

        email_field = browser.find_element(By.XPATH, "//input[@name='USER_LOGIN']")
        email_field.send_keys("wohocid569@qianhost.com")
        time.sleep(3)

        password_field = browser.find_element(By.XPATH, "//input[@name='USER_PASSWORD']")
        password_field.send_keys("Qwerty123456")
        time.sleep(3)

        login_button = browser.find_element(By.XPATH, "//input[@value='Увійти']")
        login_button.click()

        message = WebDriverWait(browser, 5).until_not(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='s-modal__inner done']"))
        )
        time.sleep(10)

        
        item_account_button = browser.find_element(By.XPATH, "//a[@class='s-header__item-icon']//parent::div[@class='s-header__item -account']")
        item_account_button.click()
        logout_button = browser.find_element(By.XPATH, "//a[@href='/ua/?logout=yes']")
        logout_button.click()
    finally:
        browser.quit()
        print("Browser quit")
