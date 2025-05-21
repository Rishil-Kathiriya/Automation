import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

def get_working_proxy():
    url = 'https://free-proxy-list.net/'
    print("Scraping the Free proxy...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        ip = cols[0].text.strip()
        port = cols[1].text.strip()
        https = cols[6].text.strip()

        if https.lower() == 'yes':
            proxy = f"http://{ip}:{port}"
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }
                print(f"Testing the proxy: {proxy}")
                r = requests.get("https://www.amazon.com", proxies={"http": proxy, "https": proxy}, headers=headers, timeout=5)
                if r.status_code == 200:
                    print(f"Working proxy found: {proxy}")
                    return proxy
            except:
                continue
    return None

search_element="Laptop" #input("Enter Product to Search : ")
website="Amazon" #input("In Which Website You Want to Search : ")
proxy = get_working_proxy()
if not proxy:
    print("No working proxy found. Exiting.")
    exit()

ua = UserAgent()
user_agent = ua.random

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.page_load_strategy = 'eager'  

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(20)  

try:
    print("Open httpbin.org for verifying IP...")
    driver.get("http://httpbin.org/ip")
    time.sleep(3)

    print("Open Amazon.com...")
    driver.get(f"https://www.{website}.com")
    time.sleep(15) 

    count=1
    try:
        for i in range(1,21):
            driver.get(f"https://www.amazon.com/s?k={search_element}&page={i}&xpid=RBeBtoEssQWu1&crid=1DORKX936N1UL&qid=1747726685&sprefix=apto%2Caps%2C376&ref=sr_pg_2")
            ele=driver.find_elements(By.CLASS_NAME, "puis-card-container")
            print(f"{len(ele)} Item Found..")
            for e in ele:
                d=e.get_attribute("outerHTML")
                with open(f"data/{search_element}{count}.html",'w',encoding='utf-8') as file:
                    file.write(d)
                    count+=1
        time.sleep(1)
    except Exception as e:
        print("Elemnt is Not Found :", e)

except Exception as e:
    print("Error in browsing:", e)

finally:
    print("Quitting The browser.")
    driver.quit()
