import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент формы регистрации
        self.registration_form = RegistrationFormComponent(page)

        # Элементы страницы
        self.title = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login link')

    # Метод для нажатия на кнопку "Registration"
    def click_registration_button(self):
        self.registration_button.click()

    # Метод для нажатия на ссылку "Login"
    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
