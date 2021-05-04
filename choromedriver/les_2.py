from selenium import webdriver
from time import sleep
import random
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"

user_agents_lists = [
    "hello_world",
    "best_of_best",
    "python_today"
]

useragents= UserAgent()

#options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument(f"user-agent={random.choice(user_agents_lists)}") # можно менять через list
# options.add_argument(f"user-agent={useragents.opera}") # можно вызывать как определенный браузер
options.add_argument(f"user-agent={useragents.random}")

# создаем браузер, задаем абсолютный путь до драйвера
driver = webdriver.Chrome(
    executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\chromedriver.exe",
    options=options)
sleep(1)


try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent?utm_source=whatismybrowsercom&utm_medium=internal&utm_campaign=detect-index")
    sleep(5)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
