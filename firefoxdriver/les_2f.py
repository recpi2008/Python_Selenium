from selenium import webdriver
from time import sleep
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"

useragents= UserAgent()

#options
options = webdriver.FirefoxOptions()

# change user_agent
options.set_preference("general.useragent.override", useragents.random) #перезаписываем user_agent

driver = webdriver.Firefox(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\firefoxdriver\\geckodriver.exe",
    options=options)

try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent?utm_source=whatismybrowsercom&utm_medium=internal&utm_campaign=detect-index")
    sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

