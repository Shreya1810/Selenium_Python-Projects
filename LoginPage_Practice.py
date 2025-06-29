import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR , "input[name = 'name']").send_keys('Shreya Sinha')


email = driver.find_element(By.NAME, "email")
email.send_keys('hello@gmail.com')

password = driver.find_element(By.ID, "exampleInputPassword1")
password.send_keys('123456')


driver.find_element(By.ID, "exampleCheck1").click()
#Select sex from dropdown list
#driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']/option[text()='Female']").click()

# Select static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text('Female')
time.sleep(5)
dropdown.select_by_index(0)

#Click on radiobutton
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.NAME,"bday" ).send_keys('10/18/1999')

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('Hello again')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message



#close the browser
driver.quit()