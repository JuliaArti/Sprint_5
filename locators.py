from selenium.webdriver.common.by import By

class Locators:

    # Кнопка "Войти в аккаунт"
    login_button_main = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка "Личный кабинет"
    personal_account_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    
    # "Конструктор"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")

    # Логотип "stellar burgers"
    logo_stellar_burgers = (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']") 

    # Раздел "Булки"
    inscription_buns = (By.XPATH, "//span[text()='Булки']")

    # Раздел "Булки" активен
    inscription_buns_active = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']")
    
    # Раздел "Соусы"
    inscription_sauce = (By.XPATH, "//span[text()='Соусы']")

    # Раздел "Соусы" активен
    inscription_sauce_active = ((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']"))

    # Раздел "Начинка"
    inscription_fillings = (By.XPATH, "//span[text()='Начинки']")

    # Раздел "Начинка" активен
    inscription_fillings_active = ((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']"))


    # Поле "Email"
    input_field_email = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")

    # Поле "Пароль"
    input_field_password = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")

    # Кнопка "Войти"
    button_entrance = (By.XPATH, "//button[text()='Войти']")

    # Кнопка "Войти" (Регистрация/Востан.пароля)
    button_entrance_register = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Ссылка "Зарегистрироваться"
    link_register = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/register']")

    # Кнопка "Зарегестироваться"
    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']" )

    # Поле "Имя"
    input_field_user_name = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")

    # Ссылка "Востановить пароль"
    link_password_recovery = (By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']")     
    
    # "Некорректный пароль"
    error_password = (By.XPATH, "//p[text()='Некорректный пароль']")

    # Кнопка "Выход"
    button_exit = (By.XPATH, "//button[text()='Выход']")

    # Филе Люминесцентного тетраодонтимформа
    file_lumin = (By.XPATH, "//p[text()='Филе Люминесцентного тетраодонтимформа']")

    