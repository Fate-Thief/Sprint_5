class ByLocators:

    SIGN_IN_ACCOUNT_BUTTON = '//*[@id="root"]//button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    SIGN_IN_H2_TEXT = '//*[@id="root"]//h2[text()="Вход"]'  # Заголовок Вход на странице входа в аккаунт
    SIGN_IN_EMAIL = '//*[@id="root"]//fieldset[1]//input[@name="name"]'  # Поле ввода e-mail на странице входа
    SIGN_IN_PASSWORD = '//*[@id="root"]//fieldset[2]//input[@type="password"]'  # Поле ввода пароля на странице входа
    SIGN_IN_BUTTON = '//*[@id="root"]//button[text()="Войти"]'
    SIGN_IN_LINK = '//*[@id="root"]//a[@href="/login"]'

    REGISTRATION_LINK = '//*[@id="root"]//a[text()="Зарегистрироваться"]'  # Ссылка на страницу "Зарегестрироваться"
    REGISTRATION_H2_TEXT = '//*[@id="root"]//h2[text()="Регистрация"]'  # Заголовок Регистрация на странице регистрации
    REGISTRATION_NAME_INPUT = '//*[@id="root"]//fieldset[1]//input[@name="name"]'  # Поле ввода имени пользователя на странице регистрации
    REGISTRATION_EMAIL_INPUT = '//*[@id="root"]//fieldset[2]//input[@name="name"]'  # Поле ввода e-mail на странице регистрации
    REGISTRATION_PASSWORD_INPUT = '//*[@id="root"]//fieldset[3]//input[@name="Пароль"]'  # Поле ввода пароля на странице регистрации
    REGISTRATION_BUTTON = '//*[@id="root"]//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться" на странице регистрации

    PERSONAL_ACCOUNT_LINK = '//*[@id="root"]//a[@href="/account"]'
    RESTORE_PASSWORD_LINK = '//*[@id="root"]//a[text()="Восстановить пароль"]'
    LOGO_BUTTON_LINK = '//*[@id="root"]/div/header/nav/div/a[@href="/"]'
    EXIT_BUTTON = '//*[@id="root"]//*[(@type="button") and (text()="Выход")]'

    CONSTRUCTOR_HEADER = '//*[@id="root"]//h1[text()="Соберите бургер"]'
    CONSTRUCTOR_BUNS_DIV = '//*[@id="root"]//span[text()="Соусы"]/parent::div'
    CONSTRUCTOR_BUNS_H2_TEXT = '//*[@id="root"]//h2[text()="Булки"]'
    CONSTRUCTOR_DIPS_DIV = '//*[@id="root"]//span[text()="Начинки"]/parent::div'
    CONSTRUCTOR_SAUCES_H2_TEXT = '//*[@id="root"]//h2[text()="Соусы"]'





