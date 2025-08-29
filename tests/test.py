from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# Регистрация
driver.get("https://stellarburgers.nomoreparties.site")

driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
time.sleep(5)
inputs = driver.find_elements(By.XPATH, "//input")
inputs[0].send_keys("Юлия")
time.sleep(5)
inputs = driver.find_elements(By.XPATH, "//input")
inputs[1].send_keys("JuliaArtishcheva129@ya.ru")
time.sleep(5)
inputs = driver.find_elements(By.XPATH, "//input")
inputs[2].send_keys("zxcvb123")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "button_button_type_primary__1O7Bx").click()
time.sleep(5)
driver.quit()