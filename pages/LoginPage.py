from selenium.webdriver.common.by import By


class LoginPage:
    PAGE_URL = "https://www.saucedemo.com/"
    PAGE_TITLE_LOGO = By.ID, "login_logo"
    USERNAME_FIELD = By.ID, "user-name"
    PASSWORD_FIELD = By.ID, "password"
    LOGIN_BUTTON = By.ID, "login-button"
    LOGIN_USERNAMES_LABEL = By.ID, "login_credentials"
    LOGIN_PASSWORD = By.ID, "login_password"
    PASSWORDS_LABEL = By.CSS_SELECTOR, "[data-test='login-password']"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def get_login_usernames(self):
        return self.driver.find_element(*self.LOGIN_USERNAMES_LABEL).text

    def write_on_username(self, username_input):
        user_name_field = self.driver.find_element(*self.USERNAME_FIELD)
        user_name_field.clear()
        user_name_field.send_keys(username_input)

    def write_on_password(self, password_input):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password_input)

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_password(self):
        return self.driver.find_element(*self.PASSWORDS_LABEL).text
