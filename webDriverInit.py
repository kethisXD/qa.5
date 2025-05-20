import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    service = Service(executable_path="/usr/bin/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver