class ByLocators:
    SIGN_IN_ACCOUNT_BUTTON = '//button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    SIGN_IN_H2_TEXT = '//h2[text()="Вход"]'  # Заголовок Вход на странице входа в аккаунт
    SIGN_IN_EMAIL = '//fieldset[1]//input[@name="name"]'  # Поле ввода e-mail на странице входа
    SIGN_IN_PASSWORD = '//fieldset[2]//input[@type="password"]'  # Поле ввода пароля на странице входа
    SIGN_IN_BUTTON = '//button[text()="Войти"]'
    SIGN_IN_LINK = '//a[@href="/login"]'
    SIGN_IN_ORDER_BUTTON = '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'

    REGISTRATION_LINK = '//a[text()="Зарегистрироваться"]'  # Ссылка на страницу "Зарегестрироваться"
    REGISTRATION_H2_TEXT = '//h2[text()="Регистрация"]'  # Заголовок Регистрация на странице регистрации
    REGISTRATION_NAME_INPUT = '//fieldset[1]//input[@name="name"]'  # Поле ввода имени пользователя на странице регистрации
    REGISTRATION_EMAIL_INPUT = '//fieldset[2]//input[@name="name"]'  # Поле ввода e-mail на странице регистрации
    REGISTRATION_PASSWORD_INPUT = '//fieldset[3]//input[@name="Пароль"]'  # Поле ввода пароля на странице регистрации
    REGISTRATION_BUTTON = '//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться" на странице регистрации

    PERSONAL_ACCOUNT_LINK = '//a[@href="/account"]'
    RESTORE_PASSWORD_LINK = '//a[text()="Восстановить пароль"]'
    RESTORE_PASSWORD_BUTTON = '//div/main/div/h2'
    LOGO_BUTTON_LINK = '//div/header/nav/div/a[@href="/"]'
    PROFILE_LINK = '//nav/a[@class = "AppHeader_header__link__3D_hX"]'
    EXIT_BUTTON = '//*[(@type="button") and (text()="Выход")]'

    CONSTRUCTOR_HEADER = '//h1[text()="Соберите бургер"]'
    CONSTRUCTOR_BUNS_DIV = '//span[text()="Соусы"]/parent::div'
    CONSTRUCTOR_BUNS_H2_TEXT = '//h2[text()="Булки"]'
    CONSTRUCTOR_DIPS_DIV = '//span[text()="Начинки"]/parent::div'
    CONSTRUCTOR_SAUCES_H2_TEXT = '//h2[text()="Соусы"]'
    CONSTRUCTOR_SAUCES_SPAN = '//*[contains(@class,"tab_tab_type_current")]/span'
