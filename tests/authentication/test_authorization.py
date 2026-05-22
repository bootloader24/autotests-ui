import pytest  # Импортируем библиотеку pytest

from pages.authentication.login_page import LoginPage  # Импортируем LoginPage


@pytest.mark.authorization
@pytest.mark.regression
class TestAuthorization:
    # Передаём три набора параметров
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.check_visible(email='', password='')
        login_page.login_form.fill(email=email, password=password)  # Заполняем форму авторизации
        login_page.click_login_button()  # Нажимаем кнопку "Login"
        login_page.check_visible_wrong_email_or_password_alert()  # Проверяем наличие сообщения об ошибке
