# работа в фоновом режиме
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # используем нажатие клавиш
from time import sleep
import random
# from data_auth import vk_password, vk_login
from data_auth import ins_login, ins_pass
import pickle


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36")

# disable webdriver mode
# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless") # первый способ
options.headless = True



driver = webdriver.Chrome(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\chromedriver.exe",
    options=options
)


try:
    driver.get("https://www.youtube.com/")
    print("перешли на ютюб")
    sleep(3)
    driver.get("https://yandex.ru/")
    print("перешли на янд")
    sleep(3)
    #.......

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()