from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
import math

CHROME_DRIVER_PATH = "Your Chrome Driver Absolute Path "
SIMILAR_ACCOUNT = "Name of account that you want to follow it's followers"
USERNAME = "Your Instagram Username"
PASSWORD = "Your Instagram Password"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        time.sleep(2)
        not_now_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(4)
        for i in range(10):
            scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in follow_buttons:
            if button.text == "Follow":
                button.click()
                time.sleep(2.5)


bot = InstaFollower(driver_path=CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
