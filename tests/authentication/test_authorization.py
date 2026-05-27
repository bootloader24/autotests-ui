import allure
import pytest  # Импортируем библиотеку pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.login_page import LoginPage  # Импортируем LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    # Группировка для исключения конфликта тестов при их параллельном запуске
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        # Переход на страницу регистрации
        registration_page.visit(AppRoute.REGISTRATION)
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        # Клик по кнопке "Logout"
        dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        login_page.login_form.fill(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    # Группировка для исключения конфликта тестов при их параллельном запуске
    @pytest.mark.xdist_group(name="authorization-group")
    # Передаём три набора параметров
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.check_visible(email='', password='')
        login_page.login_form.fill(email=email, password=password)  # Заполняем форму авторизации
        login_page.click_login_button()  # Нажимаем кнопку "Login"
        login_page.check_visible_wrong_email_or_password_alert()  # Проверяем наличие сообщения об ошибке

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
