import pytest
from selenium.webdriver.common.by import By
from conftest import *
import time
import random


LOGIN_ADMIN = "user"
PASS_ADMIN = "bitnami"


# 1
def test_add_category(driver):
    driver.get("http://127.0.0.1:8081/administration")
    driver.find_element(By.ID, "input-username").send_keys(LOGIN_ADMIN)
    driver.find_element(By.ID, "input-password").send_keys(PASS_ADMIN)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()
    try:
        driver.find_element(By.XPATH, "//*[@id=\"button-menu\"]").click()
    except:
        pass
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/ul/li[1]/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"input-name-1\"]").send_keys("Devices")
    driver.find_element(By.ID, "input-meta-title-1").send_keys("megaTag")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[3]/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"input-keyword-0-1\"]").send_keys("soooooos")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()

devices = [
    ("kb1", 'MegaTAG', "kb1.0v", random.randint(1000, 99999)),
    ("kb2", 'MegaTAG', "kb2.2v", random.randint(1000, 99999)),
    ("mouse1", 'MegaTAG', "mouse1.0v", random.randint(1000, 99999)),
    ("mouse2", 'MegaTAG', "mouse1337.0v", random.randint(1000, 99999)),
]
# 2
def test_add_mouse_keyboard(driver):
    driver.get("http://127.0.0.1:8081/administration")
    driver.find_element(By.ID, "input-username").send_keys(LOGIN_ADMIN)
    driver.find_element(By.ID, "input-password").send_keys(PASS_ADMIN)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()
    try:
        driver.find_element(By.XPATH, "//*[@id=\"button-menu\"]").click()
    except:
        pass
    
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a").click()
    for device, tag, model, seo in devices:
        # add 
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/a").click()
        #General
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[1]/a").click()
        
        driver.find_element(By.ID, "input-name-1").clear()
        driver.find_element(By.ID, "input-name-1").send_keys(device)

        driver.find_element(By.ID, "input-meta-title-1").clear()
        driver.find_element(By.ID, "input-meta-title-1").send_keys(tag)

        # Category
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[3]/a").click()
        driver.find_element(By.ID, "input-category").clear()
        driver.find_element(By.ID, "input-category").send_keys("Devices")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[3]/div[2]/div/ul/li/a").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()
        driver.find_element(By.ID, "input-model").clear()
        driver.find_element(By.ID, "input-model").send_keys(model)

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[11]/a").click()
        driver.find_element(By.ID, "input-keyword-0-1").clear()
        driver.find_element(By.ID, "input-keyword-0-1").send_keys(seo)

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()

        #End
        driver.find_element(By.ID, "button-menu").click()
        driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a").click()
        
# 3 
def test_value_shop(driver):
    driver.get("http://127.0.0.1:8081/en-gb?route=common/home")
    for device in devices:
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").clear()
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").send_keys(device[0])
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").click()
        driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/button").click()
        received = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[5]/div/div/div[2]/div/h4/a").text
        assert device[0] == received, f"Ожадиали {device[0]} получили {received}"

def test_delete_items(driver):
    driver.get("http://127.0.0.1:8081/administration")
    driver.find_element(By.ID, "input-username").send_keys(LOGIN_ADMIN)
    driver.find_element(By.ID, "input-password").send_keys(PASS_ADMIN)

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()
    
    driver.find_element(By.XPATH, "//*[@id=\"button-menu\"]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a").click()

    #write
    for device in ["kb1, mouse1"]:
        driver.find_element(By.ID, "input-name").send_keys(device)
        driver.find_element(By.ID/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a, "button-filter").click()
    
    