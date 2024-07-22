from selenium import webdriver


def get_driver():
    #Set option to make browsing easier 
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")#avoid info like low memory 
    options.add_argument("start-maximised")
    options.add_argument("disable-dev-shm-usage")#avoid issue when interactive with browser on linux machine
    options.add_argument("no-sandbox")
    options.add_experimental_option("exclude-switches", 
                                ["enable-automation"])
    options.add_experimental_option("diable-link-leature=AutomationControlled") 
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver



def main():
    driver = get_driver()
    element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]")
    return element

print(main())
