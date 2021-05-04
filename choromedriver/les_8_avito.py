# переключение вкладок
from selenium import webdriver
from time import sleep


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
    options=options)

try:
    driver.get("https://www.avito.ru/rossiya/nastolnye_kompyutery?cd=1")
    # print(driver.window_handles) # получить доспуп ко вкладкам
    print(f"Текущий URL:{driver.current_url}") # текущий URL
    sleep(5)
    # driver.implicitly_wait(5) # отличие от sleep что если нашел элемент не ждут оставшиеся время

    items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items[0].click()
    print(driver.window_handles)
    sleep(5)
    driver.switch_to.window(driver.window_handles[1]) # доступ (перемещение) к нужной вкладке, на [0] главная страница
    print(f"Текущий URL:{driver.current_url}")

    username = driver.find_element_by_class_name("seller-info-name")
    print(f"Имя пользователя:{username.text}")
    sleep(5)
    driver.close()

    driver.switch_to.window(driver.window_handles[0]) # отправляем на основную вкладку
    sleep(3)
    print(f"Текущий URL:{driver.current_url}")

    items[1].click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    sleep(4)
    print(f"Текущий URL:{driver.current_url}")
    data_user = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"Дата обьявления:{data_user.text}")
    name_product = driver.find_element_by_class_name("title-info-title-text")
    print(f"Продукт:{name_product.text}")
    price_product = driver.find_element_by_class_name("item-price-wrapper")
    print(f"Цена:{price_product.text}")
    join_user = driver.find_elements_by_class_name("seller-info-value")[1]
    print(f"Регистрация:{join_user.text}")



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()