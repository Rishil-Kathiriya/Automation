from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from time import sleep




ua = UserAgent()
fake_agent = ua.random




chrome_opt = Options()
chrome_opt.add_argument("--disable-blink-features=AutomationControlled")
chrome_opt.add_argument("--start-maximized")
chrome_opt.add_argument(f"user-agent={fake_agent}")
chrome_opt.add_argument("--ignore-certificate-errors")
chrome_opt.page_load_strategy = 'eager'


driver = None
try:
    # driver = webdriver.Chrome(options=chrome_opt)
    driver = uc.Chrome()
    driver.get('https://orteil.dashnet.org/cookieclicker/')

    cid = "bigCookie"
    cookies_id='cookies'
    product_price_prefix="productPrice"
    product_prefix="product"

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
    )
    lan = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
    lan.click()

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, cid))
    )
    cookie = driver.find_element(By.ID, cid)
    # cookie.click()

    while True:
        cookie.click()
        cookie_count=driver.find_element(By.ID,cookies_id).text.split(" ")[0]
        cookie_count=int(cookie_count.replace(",",""))

        for i in range(4):
            price=driver.find_element(By.ID,product_price_prefix + str(i)).text.replace(",","")

            if not price.isdigit():
                continue

            prod_price=int(price)

            if cookie_count >= prod_price:
                product=driver.find_element(By.ID,product_prefix + str(i))
                product.click()
                break



    # sleep(5)
except Exception as e:
    print(f"Error in Finding Element..{e}")
finally:
    if driver:
        try:
            driver.quit()  
        except Exception as e:
            print(f"Error while quitting driver:")
        


