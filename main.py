"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pyautogui
from PIL import Image
from PIL import ImageChops
import time

chrome_drive_path = "C:/opt/chromedriver_win32/chromedriver.exe"

## following code is depricated
## https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
## DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path=chrome_drive_path)
## Use follows code instead :

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

driver.get("https://elgoog.im/t-rex/")
timeout = 10
try:
    WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, '//body')))
    print( "Page is Ready" )
except:
    print( "Page is not ready" )
    exit(1)

time.sleep(1)
driver.find_element(By.TAG_NAME, "BODY").send_keys(Keys.UP)

canvas_region = (270, 396, 764, 217)
# Calling screenshot() will return an Image object
# canvas = pyautogui.screenshot(imageFilename="play_canvas.png", region=canvas_region)

obstacle_region = (376, 531, 100, 45)
#obstacle = pyautogui.screenshot(imageFilename="before.png", region=obstacle_region)
obstacle = pyautogui.screenshot(region=obstacle_region)

while True:
    diff = ImageChops.difference(obstacle, pyautogui.screenshot(region=obstacle_region))
    #diff = ImageChops.difference(obstacle, pyautogui.screenshot("after.png", region=obstacle_region))
    if diff.getbbox():
        print("hey there is an obsticle time to jump")
        driver.find_element(By.TAG_NAME, "BODY").send_keys(Keys.UP)
        obstacle = pyautogui.screenshot(region=obstacle_region)


time.sleep(1)
driver.find_element(By.TAG_NAME, "BODY").send_keys(Keys.UP)

driver.quit()