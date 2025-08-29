
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import sys
import os

# Добавляем родительскую папку в путь поиска модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import Locators
from urls import *

class Test_profile_constructor_logo: 
    
    # Тест переход из ЛК в Конструктор
    def test_acc_and_constructor(self, start_from_personal_account):
        
        driver = start_from_personal_account
        
        # Переход в раздел "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.constructor_button)
        )
        constructor_button =  driver.find_element(*Locators.constructor_button)
        constructor_button.click()
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.inscription_buns)
        )
    
    # Тест переход из ЛК на лого
    def test_acc_and_logo(self, start_from_personal_account):
        
        driver = start_from_personal_account
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.logo_stellar_burgers)
        )
        logo_stellar_burgers =  driver.find_element(*Locators.logo_stellar_burgers)
        logo_stellar_burgers.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.inscription_buns)
        )

        assert len(driver.find_elements(*Locators.inscription_buns)) > 0
   
    # Тест Конструктор переход к разделам
    def test_sections(self, driver):
        driver.get(main_site)

        # Переход к Конструктору
        constructor_button =  driver.find_element(*Locators.constructor_button)
        constructor_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site)
        )
       
        # Ждем отображения страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_fillings)
        )

        # переход к Начинкам
        inscription_fillings = driver.find_element(*Locators.inscription_fillings)
        inscription_fillings.click()

        # проверяяем активный раздел - Начинки
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_fillings_active)
        )

        # переход к Соусам
        inscription_sauce =  driver.find_element(*Locators.inscription_sauce)
        inscription_sauce.click()

        # проверяяем активный раздел - Соусы
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_sauce_active)
        )

        # переход к Булкам
        inscription_buns =  driver.find_element(*Locators.inscription_buns)
        inscription_buns.click()

        # проверяяем активный раздел - Булки
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_buns_active)
        )
        
    # Тест  переход по клику на «Личный кабинет».
    def test_personal_account(self, start_from_personal_account):

        driver = start_from_personal_account

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_exit)
        )

    