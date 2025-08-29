
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import sys
import os

# Добавляем родительскую папку в путь поиска модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generation_ep import EmailPasswordGenerator
from locators import Locators
from data import Credential
from urls import *

class Test_New_User: 

    # Тест регистрация нового пользователя
    def test_registration_new_user(self, start_from_registration_page):
        driver = start_from_registration_page

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_field_user_name)
        )

        # Заполняем форму регистрации
        name_field = driver.find_element(*Locators.input_field_user_name)
        email_field = driver.find_element(*Locators.input_field_email)
        password_field = driver.find_element(*Locators.input_field_password)


        # Генерация Email и Password
        Email_Password_Generator = EmailPasswordGenerator()
        Email_Password_Generator.generate()

        # Ввод данных
        name_field.send_keys(Credential.name)
        email_field.send_keys(Email_Password_Generator.email)
        password_field.send_keys(Email_Password_Generator.password)
        # Кликаем кнопку "Зарегистрироваться"
        button_register = driver.find_element(*Locators.button_register)
        button_register.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)
        )

        assert driver.current_url == login_site

    # Тест ошибка для некорректного пароля
    def test_password_bad(self, driver):
        driver.get(main_site)

        login_button_main = driver.find_element(*Locators.login_button_main)
        login_button_main.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)
        )
        
        # Переходим по ссылке "Зарегистрироваться"
        link_register = driver.find_element(*Locators.link_register)
        link_register.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_field_user_name)
        )
        # Заполняем форму регистрации
        name_field = driver.find_element(*Locators.input_field_user_name)
        email_field = driver.find_element(*Locators.input_field_email)
        password_field = driver.find_element(*Locators.input_field_password)

        # Генерация Email 
        Email_Password_Generator = EmailPasswordGenerator()
        Email_Password_Generator.generate()

        # Ввод данных
        name_field.send_keys(Credential.name)
        email_field.send_keys(Email_Password_Generator.email)
        password_field.send_keys(1234)
        # Кликаем кнопку "Зарегистрироваться"
        button_register = driver.find_element(*Locators.button_register)
        button_register.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(register_site)
        )   

       




    