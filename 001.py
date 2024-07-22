from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:\\Users\\saksh\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier 
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # Avoid info like low memory 
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")  # Avoid issue when interacting with browser on Linux machine
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("disable-blink-features", "AutomationControlled")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    return element.text

print(main())
