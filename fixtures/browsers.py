import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, \
    Page  # Импортируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Используем фикстуру playwright
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()
    # Закрываем браузер после выполнения тестов
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы
    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Заполняем поле "Email"
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")
    # Заполняем поле "Username"
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")
    # Заполняем поле "Password"
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")
    # Кликаем на кнопку "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")
    # Закрываем браузер
    browser.close()


@pytest.fixture
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Создаём новый контекст с указанием файла сохраненного состояния
    context = browser.new_context(storage_state="browser-state.json")
    # Передаем страницу из контекста для использования в тесте
    yield context.new_page()
    # Закрываем браузер
    browser.close()
