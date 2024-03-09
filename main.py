from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

NUM_PROFILES = 5
url = "https://tinder.com/"
FACEBOOK_EMAIL = os.environ["FACEBOOK_EMAIL"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url)
time.sleep(3)

login_button = driver.find_element(By.XPATH, '//*[@id="s1524772468"]/div/div[1]/div/main/div[1]/div/div/div/'
                                       'div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(2)

sign_in_facebook = driver.find_element(By.XPATH, '//*[@id="s1746112904"]/main/div[1]/div/div[1]/div/div/div[2]/'
                                                 'div[2]/span/div[2]/button')
sign_in_facebook.click()
time.sleep(2)

# Switch window to new pop-up window:
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys(FACEBOOK_EMAIL)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(FACEBOOK_PASSWORD, Keys.ENTER)

# input("Press Enter after you have completed the captcha: ")

time.sleep(5)
driver.switch_to.window(base_window)

share_location = driver.find_element(By.XPATH, '//*[@id="s1746112904"]/main/div[1]/div/div/div[3]/button[1]')
share_location.click()
time.sleep(1)

disallow_notifications = driver.find_element(By.XPATH, '//*[@id="s1746112904"]/main/div[1]/div/div/div[3]'
                                                           '/button[2]')
disallow_notifications.click()
time.sleep(10)


for num in range(NUM_PROFILES):
    time.sleep(2)
    webpage = driver.find_element(By.TAG_NAME, "html")
    # Switch to Keys.ARROW_RIGHT to swipe right (indicate interest) in another person's tinder profile.
    webpage.send_keys(Keys.ARROW_LEFT)
