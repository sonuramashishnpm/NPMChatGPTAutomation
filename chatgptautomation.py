from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

extra_prompt=input("Enter Your Query:")
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"
    })
wait = WebDriverWait(driver, 30)

url="https://chatgpt.com/"
driver.maximize_window()
driver.get(url)
time.sleep(3)

cookies=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/button[3]")
cookies.click()
time.sleep(2)

prompt=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/main/div/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div")
time.sleep(2)
prompt.send_keys(extra_prompt)
time.sleep(2.5)
prompt.send_keys(Keys.RETURN)
time.sleep(10)

response=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/div/div[1]/div/div/div[2]/article[2]")
time.sleep(3)
print(response.text)
