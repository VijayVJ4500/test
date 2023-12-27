from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
result = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(result)
assert count > 0
for results in result:
    results.find_element(By.XPATH, "div/button").click()
    time.sleep(2)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(2)
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
    print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, " .totAmt").text)
assert sum == totalAmount

discount = 0.10
discountamount= totalAmount * (1-discount)
print(discountamount)
discounted = driver.find_element(By.CSS_SELECTOR ,".discountPerc")

driver.find_element(By.CSS_SELECTOR, " input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
time.sleep(2)

driver.find_element(By.XPATH, " //button[normalize-space()='Apply']").click()
time.sleep(2)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
time.sleep(2)
