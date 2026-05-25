import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, \
    Page  # Импортируем класс страницы, будем использовать его для аннотации типов

from config import settings
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())  # Создание контекста
    page = context.new_page()  # Создание страницы

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    # Переходим на страницу регистрации
    registration_page.visit(AppRoute.REGISTRATION)
    # Заполняем форму регистрации
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    # Кликаем на кнопку "Registration"
    registration_page.click_registration_button()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path=settings.browser_state_file)
    # Закрываем браузер
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,  # В данном случае request.node.name содержит название текущего автотеста
        storage_state=settings.browser_state_file
    )
