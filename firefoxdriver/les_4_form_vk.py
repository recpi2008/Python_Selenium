from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from data_auth import vk_password

# options
options = webdriver.FirefoxOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0")

driver = webdriver.Firefox(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\firefoxdriver\\geckodriver.exe",
    options=options)


try:
    driver.get("https://vk.com/")
    sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear() #очищает поле
    email_input.send_keys("Recpi2008@yandex.ru") # заполняем поле
    sleep(5)
    pass_input = driver.find_element_by_id("index_pass")
    pass_input.clear()
    pass_input.send_keys(vk_password)
    sleep(3)
    pass_input.send_keys(Keys.ENTER)

    # login_button= driver.find_element_by_id("index_login_button").click() # первый вариант нажать на кнопку

    sleep(10)

    news_link = driver.find_element_by_id("l_nwsf").click()
    sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()