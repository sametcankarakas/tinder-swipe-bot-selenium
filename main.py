from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_driver_path = r"C:\Users\Samet\AppData\Local\Programs\Python\Python310\chromedriver.exe"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://tinder.com/")
time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()
time.sleep(2)
facebook_log_in = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_log_in.click()
time.sleep(2)
windows_list = driver.window_handles
tinder_screen = windows_list[0]
facebook_log_in = windows_list[1]
driver.switch_to.window(facebook_log_in)
mail_address_input = driver.find_element(By.NAME, 'email')
mail_address_input.send_keys("**@gmail.com")
time.sleep(1)
input_password = driver.find_element(By.NAME, 'pass')
input_password.send_keys("***")
time.sleep(1)
login_button_facebook = driver.find_element(By.NAME, "login")
login_button_facebook.click()
time.sleep(10)
driver.switch_to.window(tinder_screen)
allow_location = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(1)
allow_location = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(10)

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                '//*[@id="q-184954025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        time.sleep(2)

driver.quit()