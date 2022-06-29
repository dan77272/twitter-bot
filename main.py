from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:\Development\chromedriver.exe")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"down: {self.down.text}")
        self.up = self.driver.find_element(By.XPATH,
                                                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(f"up: {self.up.text}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH,
                                           '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down.text}/{self.up.text} when I pay for 1000down/1000up?")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
