from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#Click on Shop link
#driver.find_element(By.LINK_TEXT,"Shop").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
product_list = driver.find_elements(By.XPATH,"//div[@class='Card h-100']")

for product in product_list:
    product_name = product.find_element(By.XPATH,"div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

# click on checkout
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

# click on checkout to proceed
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

# Input country name in autosuggestive dynamic dropdown
driver.find_element(By.ID, "country").send_keys("ind")

# explicit wait to wait until dropdown options are visible according to given literals
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()
#click on checkbox and then proceed
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

# grab success message and put asssertion
success_msg = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in success_msg 
#close browser
driver.quit()