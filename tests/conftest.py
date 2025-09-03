import pytest
from selenium import webdriver
from urls import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generation_ep import EmailPasswordGenerator
from data import Credential 


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
    
@pytest.fixture
def start_after_login(start_from_login_page):
    driver = start_from_login_page
    

    # Ищем поля для авторизации
    driver.find_element(*Locators.input_field_email).send_keys(Credential.email)
    driver.find_element(*Locators.input_field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
    
    return driver

# попадаем в лк
@pytest.fixture
def start_from_personal_account(start_after_login):
    driver = start_after_login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.personal_account_button)
    )
    personal_account_button = driver.find_element(*Locators.personal_account_button)
    personal_account_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(profile_site)
    )

    return driver

# регистрация
@pytest.fixture
def start_from_registration_page(start_from_login_page):
    driver = start_from_login_page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.link_register)
    )
    # Переход на форму регистрации
    link_register = driver.find_element(*Locators.link_register)
    link_register.click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(register_site)
    )

    return driver


@pytest.fixture
def start_from_login_page(driver):
    # Открываем стартовую страницу и переходим в ЛК
    driver.get(main_site)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.personal_account_button)
    )
    personal_account_button = driver.find_element(*Locators.personal_account_button)
    personal_account_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(login_site)
    )

    return driver

    




    




