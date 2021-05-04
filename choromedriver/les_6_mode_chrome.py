# отключение режима webdriver
from selenium import webdriver
from time import sleep



# options
options = webdriver.ChromeOptions()
# user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36")

# disable webdriver mode
# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\chromedriver.exe",
    options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()