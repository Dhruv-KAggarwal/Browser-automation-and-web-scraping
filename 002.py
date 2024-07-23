from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('C:\\Users\\saksh\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier 
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # Avoid info like low memory 
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")  # Avoid issue when interacting with browser on Linux machine
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)  # This option should be used instead
    options.add_argument("--disable-blink-features=AutomationControlled")  # Correct usage of disable-blink-features
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver



def clean_text(text):
    """Extract only the temperature from the text """
    output = float(text.split(": ")[1])
    return output




def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())