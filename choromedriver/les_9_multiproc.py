
from selenium import webdriver
from time import sleep
from multiprocessing import Pool
import random


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36")

# disable webdriver mode
# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless") # первый способ
# options.headless = True

# urls_list = ["https://stackoverflow.com", "https://instagram.com", "https://vk.com"]



# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\chromedriver.exe",
#             options=options)
#         driver.get(url=url)
#         sleep(5)
#         driver.get_screenshot_as_file(f"C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\media\\{url.split('//')[1]}.png")
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
# if __name__=='__main__':
#     p=Pool(processes=3)
#     p.map(get_data, urls_list)


def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\ivane\\eles\\Python_Selenium\\choromedriver\\chromedriver.exe",
            options=options)
        driver.get(url=url)
        sleep(5)
        driver.find_element_by_class_name("lazyload-wrapper").find_element_by_class_name("item-video-container").click()
        sleep(random.randrange(3,10))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__=='__main__':
    process_count = int(input("Введи количество потоков:\n"))
    url = input("Введи url:\n")
    urls_list = [url] * process_count
    print(urls_list)
    p=Pool(processes=process_count)
    p.map(get_data, urls_list)
