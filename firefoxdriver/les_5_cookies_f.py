from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from data_auth import ins_login, ins_pass
import pickle


# options
options = webdriver.FirefoxOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0")

driver = webdriver.Firefox(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\firefoxdriver\\geckodriver.exe",
    options=options)


try:
    driver.get("https://www.instagram.com/")
    sleep(5)

    # email_input = driver.find_element_by_name("username")
    # email_input.clear() #очищает поле
    # email_input.send_keys(ins_login) # заполняем поле
    # sleep(5)
    # pass_input = driver.find_element_by_name("password")
    # pass_input.clear()
    # pass_input.send_keys(ins_pass)
    # sleep(3)
    # pass_input.send_keys(Keys.ENTER)
    # sleep(10)
    #
    # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{ins_login}_cookies","wb")) # создаем файл с куками

    for cookie in pickle.load(open(f"{ins_login}_cookies", "rb")):
        driver.add_cookie(cookie)
    sleep(5)
    driver.refresh()
    sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
