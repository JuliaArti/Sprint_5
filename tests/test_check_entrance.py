# вход через ЛК и кнопка Войти в акк

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import sys
import os

# Добавляем родительскую папку в путь поиска модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import Locators
from data import Credential
from urls import *

class Test_Authorization:

    # Тест авторизация через Войти в акк на гл странице
    def test_login_enter_acc(self, driver):
        driver.get(main_site)
        
        login_button_main = driver.find_element(*Locators.login_button_main)
        login_button_main.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)
        )

        assert self.Login(driver)

    # Тест авторизация через ЛК
    def test_successful_login(self, start_after_login):
        driver = start_after_login
        assert driver.current_url == main_site  

    # Тест вход в акк через копку в форме регистрации   
    def test_registration_form(self, start_from_registration_page):

        driver = start_from_registration_page
        #  Переход на форму авторизации
        button_entrance_register = driver.find_element(*Locators.button_entrance_register)
        button_entrance_register.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)   
        )

        assert self.Login(driver)
    
    # Тест вход через кнопку в форме востановления пароля
    def test_restore_password_login(self, start_from_login_page):

        driver = start_from_login_page
        # Переход на форму востановления пароля
        link_password_recovery = driver.find_element(*Locators.link_password_recovery)
        link_password_recovery.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(forgot_password)
        )

        #  Переход на форму авторизации
        button_entrance_register = driver.find_element(*Locators.button_entrance_register)
        button_entrance_register.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)   
        )

        assert self.Login(driver)
    
    def Login(self, driver):

        driver.find_element(*Locators.input_field_email).send_keys(Credential.email)
        driver.find_element(*Locators.input_field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        return driver.current_url == main_site
         
    # Тест выход     
    def test_logout(self, start_from_personal_account):
        driver = start_from_personal_account

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.button_exit)
        )
       
        # Нажатие кнопки выхода
        exit_button = driver.find_element(*Locators.button_exit)
        exit_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)
        )

        assert driver.current_url == login_site
        
